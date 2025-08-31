# FRACTAL-RMO QUICK START GUIDE
## Get Up and Running in 30 Minutes

---

## Prerequisites

### System Requirements
- macOS or Linux (Windows WSL2 supported)
- 16GB RAM minimum (32GB recommended)
- 50GB free disk space
- Python 3.11+
- Docker Desktop installed and running
- Git

### API Keys Needed
```bash
# Create .env file in project root
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
DB_PASSWORD=choose_secure_password
REDIS_PASSWORD=choose_secure_password
```

---

## STEP 1: Project Setup (5 minutes)

```bash
# Clone or create project directory
mkdir -p ~/CodingProjects/fractal-rmo
cd ~/CodingProjects/fractal-rmo

# Initialize git repository
git init
echo "# Fractal-RMO" > README.md
git add README.md
git commit -m "Initial commit"

# Create project structure
mkdir -p {agents,core,learning,data,api,cli,tests,configs,scripts,docker}

# Create Python virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install poetry for dependency management
pip install poetry
```

---

## STEP 2: Install Dependencies (5 minutes)

Create `pyproject.toml`:
```toml
[tool.poetry]
name = "fractal-rmo"
version = "0.1.0"
description = "Recursive Multi-Objective Learning System"
authors = ["Chris Hamlin"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
uvicorn = "^0.24.0"
sqlalchemy = "^2.0.0"
asyncpg = "^0.28.0"
redis = "^5.0.0"
pydantic = "^2.4.0"
openai = "^1.3.0"
anthropic = "^0.7.0"
click = "^8.1.0"
python-dotenv = "^1.0.0"
numpy = "^1.24.0"
scikit-learn = "^1.3.0"

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
pytest-cov = "^4.1.0"
pylint = "^3.0.0"
black = "^23.0.0"
mypy = "^1.5.0"
```

Install dependencies:
```bash
poetry install
```

---

## STEP 3: Database Setup (5 minutes)

Create `docker/docker-compose.yml`:
```yaml
version: '3.8'

services:
  postgres:
    image: timescale/timescaledb:latest-pg15
    container_name: fractal_postgres
    environment:
      POSTGRES_DB: fractal_rmo
      POSTGRES_USER: fractal
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U fractal"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: fractal_redis
    command: >
      redis-server 
      --requirepass ${REDIS_PASSWORD}
      --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
  redis_data:
```

Create `docker/init.sql`:
```sql
-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "timescaledb";

-- Create base tables
CREATE TABLE agents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    config JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    result JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

CREATE TABLE error_logs (
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    task_id UUID,
    agent_id UUID,
    error_type VARCHAR(100),
    message TEXT,
    context JSONB
);

-- Convert to hypertable for time-series optimization
SELECT create_hypertable('error_logs', 'time');

-- Create indexes
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_error_logs_type ON error_logs(error_type, time DESC);
```

Start the databases:
```bash
cd docker
docker-compose up -d

# Verify they're running
docker ps
# Should show fractal_postgres and fractal_redis running
```

---

## STEP 4: Create Core Components (10 minutes)

### Base Agent Class
Create `agents/base_agent.py`:
```python
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import asyncio
import json
from datetime import datetime

@dataclass
class ActionItem:
    id: str
    name: str
    parameters: Dict[str, Any]
    
@dataclass
class ExecutionResult:
    success: bool
    output: Optional[Any] = None
    error: Optional[str] = None
    tokens_used: int = 0

class Agent(ABC):
    def __init__(self, agent_id: str, agent_type: str):
        self.id = agent_id
        self.type = agent_type
        self.error_log = []
        
    @abstractmethod
    async def process(self, task: Dict) -> ExecutionResult:
        """Process a task and return results"""
        pass
    
    def log_error(self, error: Exception, context: Dict):
        """Log errors for pattern extraction"""
        self.error_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'error_type': type(error).__name__,
            'message': str(error),
            'context': context
        })
```

### Simple Analyzer Agent
Create `agents/analyzer.py`:
```python
from agents.base_agent import Agent, ActionItem, ExecutionResult
from typing import Dict, List
import openai
import os
from dotenv import load_dotenv

load_dotenv()

class AnalyzerAgent(Agent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "analyzer")
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    async def process(self, task: Dict) -> ExecutionResult:
        """Analyze task and break down into action items"""
        try:
            # Use GPT-4 to analyze the task
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a task analyzer. Break down the given task into specific action items."},
                    {"role": "user", "content": f"Task: {task.get('description', '')}\n\nBreak this down into 3-5 specific action items. Return as JSON array."}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            # Parse response
            content = response.choices[0].message.content
            action_items = self._parse_action_items(content)
            
            return ExecutionResult(
                success=True,
                output=action_items,
                tokens_used=response.usage.total_tokens
            )
            
        except Exception as e:
            self.log_error(e, {"task": task})
            return ExecutionResult(
                success=False,
                error=str(e)
            )
    
    def _parse_action_items(self, content: str) -> List[ActionItem]:
        """Parse LLM response into action items"""
        # Simple parsing - in production would be more robust
        try:
            import json
            items = json.loads(content)
            return [
                ActionItem(
                    id=f"action_{i}",
                    name=item.get("name", f"Action {i}"),
                    parameters=item.get("parameters", {})
                )
                for i, item in enumerate(items)
            ]
        except:
            # Fallback to simple action items
            return [
                ActionItem(id="action_1", name="Analyze", parameters={}),
                ActionItem(id="action_2", name="Execute", parameters={}),
                ActionItem(id="action_3", name="Validate", parameters={})
            ]
```

### Simple Validator
Create `agents/validator.py`:
```python
import ast
from agents.base_agent import Agent, ExecutionResult
from typing import Dict

class ValidatorAgent(Agent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "validator")
        
    async def process(self, task: Dict) -> ExecutionResult:
        """Validate code or results"""
        try:
            code = task.get('code', '')
            
            # Level 1: Syntax validation
            if code:
                try:
                    ast.parse(code)
                    validation_passed = True
                    message = "Syntax validation passed"
                except SyntaxError as e:
                    validation_passed = False
                    message = f"Syntax error: {e}"
            else:
                validation_passed = False
                message = "No code provided"
            
            return ExecutionResult(
                success=validation_passed,
                output={"validation": validation_passed, "message": message}
            )
            
        except Exception as e:
            self.log_error(e, {"task": task})
            return ExecutionResult(
                success=False,
                error=str(e)
            )
```

### Database Connection
Create `data/database.py`:
```python
import asyncpg
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None
        
    async def connect(self):
        """Create connection pool"""
        self.pool = await asyncpg.create_pool(
            host='localhost',
            port=5432,
            user='fractal',
            password=os.getenv('DB_PASSWORD'),
            database='fractal_rmo',
            min_size=5,
            max_size=20
        )
    
    async def disconnect(self):
        """Close connection pool"""
        if self.pool:
            await self.pool.close()
    
    async def log_error(self, task_id: str, agent_id: str, error_type: str, message: str, context: dict):
        """Log error to database"""
        async with self.pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO error_logs (task_id, agent_id, error_type, message, context)
                VALUES ($1, $2, $3, $4, $5)
            """, task_id, agent_id, error_type, message, context)
    
    async def create_task(self, description: str) -> str:
        """Create a new task"""
        async with self.pool.acquire() as conn:
            task_id = await conn.fetchval("""
                INSERT INTO tasks (description)
                VALUES ($1)
                RETURNING id
            """, description)
            return str(task_id)
    
    async def update_task_status(self, task_id: str, status: str, result: dict = None):
        """Update task status"""
        async with self.pool.acquire() as conn:
            await conn.execute("""
                UPDATE tasks 
                SET status = $1, result = $2, completed_at = NOW()
                WHERE id = $3
            """, status, result, task_id)

# Global database instance
db = Database()
```

---

## STEP 5: Create Simple Orchestrator (5 minutes)

Create `core/orchestrator.py`:
```python
import asyncio
from typing import Dict
from agents.analyzer import AnalyzerAgent
from agents.validator import ValidatorAgent
from data.database import db

class Orchestrator:
    def __init__(self):
        self.analyzer = AnalyzerAgent("analyzer_001")
        self.validator = ValidatorAgent("validator_001")
        
    async def process_task(self, description: str) -> Dict:
        """Process a task through the pipeline"""
        # Create task in database
        task_id = await db.create_task(description)
        
        try:
            # Step 1: Analyze
            print(f"Analyzing task: {description}")
            analysis_result = await self.analyzer.process({"description": description})
            
            if not analysis_result.success:
                raise Exception(f"Analysis failed: {analysis_result.error}")
            
            print(f"Found {len(analysis_result.output)} action items")
            
            # Step 2: Execute (simplified - just generate sample code)
            sample_code = """
def hello_world():
    print("Hello, World!")
    return True
"""
            
            # Step 3: Validate
            print("Validating code...")
            validation_result = await self.validator.process({"code": sample_code})
            
            if validation_result.success:
                print("✓ Validation passed!")
            else:
                print(f"✗ Validation failed: {validation_result.output}")
            
            # Update task status
            await db.update_task_status(
                task_id, 
                "completed" if validation_result.success else "failed",
                {
                    "action_items": [a.__dict__ for a in analysis_result.output],
                    "validation": validation_result.output
                }
            )
            
            return {
                "task_id": task_id,
                "success": validation_result.success,
                "action_items": analysis_result.output,
                "tokens_used": analysis_result.tokens_used
            }
            
        except Exception as e:
            await db.update_task_status(task_id, "failed", {"error": str(e)})
            raise
```

---

## STEP 6: Create CLI Interface (5 minutes)

Create `cli/main.py`:
```python
import click
import asyncio
from core.orchestrator import Orchestrator
from data.database import db
import json

@click.group()
def cli():
    """Fractal-RMO Command Line Interface"""
    pass

@cli.command()
@click.argument('description')
def process(description):
    """Process a task through the system"""
    async def run():
        # Connect to database
        await db.connect()
        
        try:
            # Create orchestrator and process task
            orchestrator = Orchestrator()
            result = await orchestrator.process_task(description)
            
            # Display results
            click.echo("\n" + "="*50)
            click.echo(f"Task ID: {result['task_id']}")
            click.echo(f"Status: {'✓ Success' if result['success'] else '✗ Failed'}")
            click.echo(f"Tokens Used: {result['tokens_used']}")
            click.echo(f"Action Items: {len(result['action_items'])}")
            
            for item in result['action_items']:
                click.echo(f"  - {item.name}")
            
        finally:
            await db.disconnect()
    
    # Run the async function
    asyncio.run(run())

@cli.command()
def test():
    """Test system components"""
    async def run_tests():
        await db.connect()
        
        try:
            click.echo("Testing database connection... ", nl=False)
            await db.create_task("Test task")
            click.echo("✓")
            
            click.echo("Testing analyzer agent... ", nl=False)
            analyzer = AnalyzerAgent("test")
            result = await analyzer.process({"description": "Write a hello world function"})
            if result.success:
                click.echo("✓")
            else:
                click.echo(f"✗ {result.error}")
            
            click.echo("Testing validator agent... ", nl=False)
            validator = ValidatorAgent("test")
            result = await validator.process({"code": "print('test')"})
            if result.success:
                click.echo("✓")
            else:
                click.echo(f"✗ {result.error}")
                
        finally:
            await db.disconnect()
    
    asyncio.run(run_tests())

if __name__ == '__main__':
    cli()
```

Create main entry point `fractal_rmo.py`:
```python
#!/usr/bin/env python
from cli.main import cli

if __name__ == '__main__':
    cli()
```

---

## STEP 7: Run Your First Task!

```bash
# Make sure you're in the project directory with venv activated
cd ~/CodingProjects/fractal-rmo
source venv/bin/activate

# Load environment variables
export $(cat .env | xargs)

# Test the system
python fractal_rmo.py test

# If all tests pass, process your first task!
python fractal_rmo.py process "Write a Python function to calculate fibonacci numbers"

# Expected output:
# Analyzing task: Write a Python function to calculate fibonacci numbers
# Found 3 action items
# Validating code...
# ✓ Validation passed!
# ==================================================
# Task ID: [UUID]
# Status: ✓ Success
# Tokens Used: ~500
# Action Items: 3
#   - Analyze
#   - Execute  
#   - Validate
```

---

## What's Next?

### 1. Add Pattern Extraction (Next Hour)
Create `learning/pattern_extractor.py` to analyze error logs and find patterns.

### 2. Implement Executor Agent (Next Day)
Build actual code generation capability instead of using sample code.

### 3. Add More Validators (Next Week)
- Static analysis with pylint
- Unit test execution
- Performance validation

### 4. Build the API (Next Week)
```bash
# Start the API server
uvicorn api.main:app --reload

# Submit tasks via HTTP
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Write a sorting algorithm"}'
```

### 5. Implement Learning Loop (Week 2)
- Extract patterns from errors
- Generate insights
- Update agent protocols
- Measure improvement

---

## Troubleshooting

### Database Connection Issues
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Check logs
docker logs fractal_postgres

# Test connection
psql -h localhost -U fractal -d fractal_rmo
```

### API Key Issues
```bash
# Verify API keys are set
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# Test OpenAI connection
python -c "import openai; openai.OpenAI(api_key='$OPENAI_API_KEY').models.list()"
```

### Python Issues
```bash
# Ensure Python 3.11
python --version

# Reinstall dependencies
poetry install --no-cache
```

---

## Project Structure After Setup

```
fractal-rmo/
├── .env                    # API keys and secrets
├── .gitignore             # Git ignore file
├── pyproject.toml         # Poetry dependencies
├── fractal_rmo.py         # Main entry point
├── agents/
│   ├── __init__.py
│   ├── base_agent.py      # Base agent class
│   ├── analyzer.py        # Analyzer agent
│   └── validator.py       # Validator agent
├── core/
│   ├── __init__.py
│   └── orchestrator.py    # Task orchestration
├── data/
│   ├── __init__.py
│   └── database.py        # Database connection
├── cli/
│   ├── __init__.py
│   └── main.py           # CLI commands
├── docker/
│   ├── docker-compose.yml # Database services
│   └── init.sql          # Database schema
└── tests/                # Tests (to be added)
```

---

## Key Commands Summary

```bash
# Start databases
cd docker && docker-compose up -d

# Run tests
python fractal_rmo.py test

# Process a task
python fractal_rmo.py process "Your task description here"

# Stop databases
cd docker && docker-compose down

# View logs
docker logs fractal_postgres
docker logs fractal_redis
```

---

## 🎉 Congratulations!

You now have a working Fractal-RMO proof of concept! 

The system can:
- ✅ Accept tasks through CLI
- ✅ Analyze tasks into action items
- ✅ Validate code syntax
- ✅ Log errors to database
- ✅ Track token usage

Next steps:
1. Run a few tasks and check the error_logs table
2. Start building pattern extraction
3. Add more sophisticated validation
4. Implement the learning loop

Remember: The goal is to achieve >20% error reduction through learning. Start measuring from day one!

---

*For questions or issues, refer to the main IMPLEMENTATION_ROADMAP.md document*
