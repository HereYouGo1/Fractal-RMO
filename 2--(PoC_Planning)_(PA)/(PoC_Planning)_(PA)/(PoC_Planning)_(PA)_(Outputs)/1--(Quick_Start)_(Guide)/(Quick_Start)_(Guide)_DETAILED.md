# FRACTAL-RMO QUICK START GUIDE - DETAILED VERSION
## Every Command Explained, Every Step Clear

---

## BEFORE YOU START - UNDERSTANDING THE BASICS

### What is Terminal?
**Terminal** (also called Command Line or Shell) is a text-based way to control your computer. Instead of clicking buttons, you type commands.

**How to open Terminal:**
- **Mac**: Press `Cmd + Space`, type "Terminal", press Enter. A black or white window appears with text.
- **Linux**: Press `Ctrl + Alt + T`
- **Windows**: You need WSL (Windows Subsystem for Linux) first. Search "Ubuntu" in Start Menu.

**Terminal basics you need to know:**
- The `$` or `%` symbol shows where you type (called the "prompt")
- After typing a command, press Enter to run it
- Use arrow keys: Up = previous command, Down = next command
- `Ctrl+C` = stop a running command
- `clear` = clean the screen when it gets messy

### What is a Virtual Environment?
Think of it like a clean room just for this project. When you install Python packages here, they won't mess with other projects on your computer. It's like having separate toolboxes for different jobs.

### What is Docker?
Docker runs programs in "containers" - isolated boxes that contain everything the program needs. We use it for databases because:
- You don't have to install PostgreSQL and Redis directly on your Mac
- You can start/stop them easily
- They won't interfere with anything else
- Easy to delete and start fresh if needed

---

## PREREQUISITES - DETAILED SETUP

### 1. Check Python Version
```bash
# Open Terminal first (see instructions above)
# Type this command to check your Python version:
python3 --version

# You should see something like: Python 3.11.5
# If you see 3.10 or lower, you need to upgrade
```

**If you need to install Python 3.11:**
```bash
# On Mac with Homebrew (install Homebrew first from brew.sh):
brew install python@3.11

# On Ubuntu/Debian Linux:
sudo apt update
sudo apt install python3.11

# Verify it worked:
python3.11 --version
```

### 2. Check Git
```bash
# Check if Git is installed:
git --version

# Should show something like: git version 2.39.2
# If "command not found", install it:

# Mac:
brew install git

# Linux:
sudo apt install git
```

### 3. Install Docker Desktop
**This is crucial - databases won't work without it!**

**For Mac:**
1. Go to https://www.docker.com/products/docker-desktop/
2. Click "Download for Mac" (choose Intel or Apple chip version)
3. Open the downloaded .dmg file
4. Drag Docker to Applications folder
5. Open Docker from Applications
6. You'll see a whale icon in your menu bar when running

**Verify Docker is working:**
```bash
# In Terminal, type:
docker --version
# Should show: Docker version 24.x.x or similar

# Test it's really working:
docker run hello-world
# Should print a success message
```

### 4. Get Your AI API Keys

**OpenAI (for GPT-4):**
1. Go to https://platform.openai.com/signup
2. Create account or login
3. Click your profile (top right) → "View API keys"
4. Click "Create new secret key"
5. **COPY IT IMMEDIATELY** - you can't see it again!
6. Save it somewhere safe temporarily

**Anthropic (for Claude):**
1. Go to https://console.anthropic.com/
2. Create account or login
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy and save it

---

## STEP 1: CREATE YOUR PROJECT (10 minutes with explanations)

### Understanding the Folder Structure
We're creating organized folders like this:
```
fractal-rmo/
├── agents/       # Your AI agents live here
├── core/         # Main orchestration logic
├── learning/     # Pattern detection code
├── data/         # Database connections
├── api/          # Web API endpoints
├── cli/          # Command-line interface
├── tests/        # Test files
├── configs/      # Settings and configuration
├── scripts/      # Helper scripts
├── docker/       # Database setup files
└── venv/         # Python virtual environment
```

### Create the Project Step by Step

```bash
# STEP 1.1: Navigate to where you want your project
# The ~ symbol means your home folder (/Users/yourname on Mac)
cd ~

# See where you are:
pwd
# Should show: /Users/yourname

# STEP 1.2: Create the project folders
# mkdir = "make directory" (create folder)
# -p = "create parent folders if needed"
mkdir -p CodingProjects/fractal-rmo

# STEP 1.3: Go into your new project folder
cd CodingProjects/fractal-rmo

# Verify you're in the right place:
pwd
# Should show: /Users/yourname/CodingProjects/fractal-rmo

# STEP 1.4: Initialize Git (version control)
# This creates a hidden .git folder that tracks all your changes
git init

# You should see: "Initialized empty Git repository..."

# STEP 1.5: Create a README file
# echo prints text, > saves it to a file
echo "# Fractal-RMO Project" > README.md

# Check the file was created:
ls
# Should show: README.md

# STEP 1.6: Save your first Git snapshot
git add README.md        # Tell Git to track this file
git commit -m "Initial commit"  # Save a snapshot with a message

# STEP 1.7: Create all project folders at once
# The {a,b,c} syntax creates multiple folders
mkdir -p agents core learning data api cli tests configs scripts docker

# Verify all folders were created:
ls -la
# Should show all 10 folders plus README.md

# STEP 1.8: Create Python virtual environment
# This creates a 'venv' folder with its own Python installation
python3.11 -m venv venv

# See what was created:
ls venv/
# Should show: bin, include, lib, etc.

# STEP 1.9: Activate the virtual environment
# This "enters" the isolated Python environment
source venv/bin/activate

# YOUR PROMPT SHOULD NOW SHOW (venv) at the beginning!
# Like this: (venv) yourname@computer:~/CodingProjects/fractal-rmo$

# If you don't see (venv), the activation failed - try again

# STEP 1.10: Upgrade pip and install Poetry
# pip is Python's package installer
# Poetry is a better package manager we'll use
pip install --upgrade pip
pip install poetry

# Verify installation:
poetry --version
# Should show: Poetry (version 1.x.x)
```

---

## STEP 2: CREATE PROJECT CONFIGURATION FILES

### Understanding Configuration Files
- **.env** = Secret passwords and API keys (never share this!)
- **pyproject.toml** = List of Python packages your project needs
- **docker-compose.yml** = Instructions for running databases

### Create the .env File for Secrets

```bash
# Make sure you're in the project folder
cd ~/CodingProjects/fractal-rmo

# Create .env file with your actual API keys
# Replace the placeholder text with your real keys!
cat > .env << 'EOF'
# API Keys - Replace with your actual keys
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx

# Database Passwords - Make up strong passwords
DB_PASSWORD=MySecurePassword123!
REDIS_PASSWORD=AnotherSecurePass456!

# Don't use these example passwords - create your own!
EOF

# Verify the file was created:
cat .env
# Should show your keys and passwords

# IMPORTANT: Add .env to .gitignore so it's never uploaded
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to gitignore for security"
```

### Create Python Dependencies File

```bash
# Create pyproject.toml file
# This lists all Python packages we need
cat > pyproject.toml << 'EOF'
[tool.poetry]
name = "fractal-rmo"
version = "0.1.0"
description = "Recursive Multi-Objective Learning System"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
# Web framework for API
fastapi = "^0.104.0"
uvicorn = "^0.24.0"

# Database connections
sqlalchemy = "^2.0.0"
asyncpg = "^0.28.0"
redis = "^5.0.0"

# AI model APIs
openai = "^1.3.0"
anthropic = "^0.7.0"

# Utilities
pydantic = "^2.4.0"
click = "^8.1.0"
python-dotenv = "^1.0.0"

# Machine learning
numpy = "^1.24.0"
scikit-learn = "^1.3.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
black = "^23.0.0"
pylint = "^3.0.0"
EOF

# Install all dependencies
# This downloads and installs all packages listed above
poetry install

# This will take 2-3 minutes and show progress
# Creates poetry.lock file with exact versions
```

---

## STEP 3: SET UP DATABASES WITH DOCKER

### Create Docker Configuration

```bash
# Navigate to docker folder
cd ~/CodingProjects/fractal-rmo/docker

# Create docker-compose.yml
# This file tells Docker what databases to run
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  # PostgreSQL - Main database for storing everything
  postgres:
    image: timescale/timescaledb:latest-pg15
    container_name: fractal_postgres
    environment:
      POSTGRES_DB: fractal_rmo
      POSTGRES_USER: fractal
      POSTGRES_PASSWORD: ${DB_PASSWORD}  # Uses password from .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"  # Makes database accessible on port 5432
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U fractal"]
      interval: 5s
      timeout: 5s
      retries: 5

  # Redis - Fast cache and message queue
  redis:
    image: redis:7-alpine
    container_name: fractal_redis
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"  # Makes Redis accessible on port 6379

volumes:
  postgres_data:  # Stores database files
  redis_data:     # Stores Redis data
EOF
```

### Create Database Schema

```bash
# Still in docker folder
# Create initial database structure
cat > init.sql << 'EOF'
-- This SQL file sets up your database tables

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- For generating unique IDs

-- Table for AI agents
CREATE TABLE agents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    config JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Table for tasks
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    result JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- Table for error logs
CREATE TABLE error_logs (
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    task_id UUID,
    agent_id UUID,
    error_type VARCHAR(100),
    message TEXT,
    context JSONB
);

-- Create indexes for faster queries
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_error_logs_type ON error_logs(error_type, time DESC);
EOF
```

### Start the Databases

```bash
# Go back to docker folder
cd ~/CodingProjects/fractal-rmo/docker

# Load environment variables from .env file
export $(cat ../.env | xargs)

# Start databases in background
# -d means "detached" (runs in background)
docker-compose up -d

# You should see:
# ✔ Network docker_default Created
# ✔ Container fractal_postgres Started
# ✔ Container fractal_redis Started

# Verify they're running:
docker ps
# Should show both fractal_postgres and fractal_redis as "Up"

# Check PostgreSQL logs (should show "database system is ready"):
docker logs fractal_postgres | tail -5

# Check Redis logs (should show "Ready to accept connections"):
docker logs fractal_redis | tail -5
```

### Test Database Connection

```bash
# Test PostgreSQL connection
# You'll need to enter the password from your .env file
docker exec -it fractal_postgres psql -U fractal -d fractal_rmo -c "SELECT 'Connected!' as status;"

# Should show:
#   status   
# -----------
#  Connected!

# Test Redis connection
docker exec -it fractal_redis redis-cli -a $REDIS_PASSWORD ping
# Should show: PONG
```

---

## STEP 4: CREATE YOUR FIRST PYTHON FILES

### Create Base Agent Class

```bash
# Go to project root
cd ~/CodingProjects/fractal-rmo

# Make sure virtual environment is active
source venv/bin/activate  # You should see (venv) in prompt

# Create the agents folder structure
cd agents

# Create __init__.py (makes folder a Python package)
touch __init__.py

# Create base_agent.py
cat > base_agent.py << 'EOF'
"""
Base Agent Class
This is the blueprint that all other agents inherit from
Like a template that defines what every agent must be able to do
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# This is a data structure for action items
# Like a recipe card with an ID, name, and parameters
@dataclass
class ActionItem:
    id: str
    name: str
    parameters: Dict[str, Any]

# This is what agents return after processing
@dataclass  
class ExecutionResult:
    success: bool  # Did it work?
    output: Optional[Any] = None  # What was produced?
    error: Optional[str] = None  # What went wrong (if anything)?
    tokens_used: int = 0  # How many AI tokens were used?

# The base Agent class - all agents inherit from this
class Agent(ABC):
    """
    Abstract base class for all agents
    ABC means this is a template - you can't use it directly
    You must create specific agent types that inherit from it
    """
    
    def __init__(self, agent_id: str, agent_type: str):
        """Initialize an agent with ID and type"""
        self.id = agent_id
        self.type = agent_type
        self.error_log = []  # Stores errors for learning
        
    @abstractmethod
    async def process(self, task: Dict) -> ExecutionResult:
        """
        Every agent must implement this method
        It takes a task and returns a result
        'async' means it can wait for things (like API calls) without blocking
        """
        pass
    
    def log_error(self, error: Exception, context: Dict):
        """
        Log errors for pattern analysis
        This is how the system learns from mistakes
        """
        self.error_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'error_type': type(error).__name__,
            'message': str(error),
            'context': context
        })
        print(f"Error logged: {error}")
EOF

echo "Created base_agent.py"
```

### Create Simple Test Script

```bash
# Go back to project root
cd ~/CodingProjects/fractal-rmo

# Create a test script to verify everything works
cat > test_setup.py << 'EOF'
#!/usr/bin/env python3
"""
Test script to verify your setup is working
Run this to make sure everything is installed correctly
"""

import sys
import os

def test_imports():
    """Test that all required packages are installed"""
    
    print("Testing package imports...")
    
    # Test each package
    packages = {
        'fastapi': 'FastAPI web framework',
        'openai': 'OpenAI API client',
        'anthropic': 'Anthropic API client',
        'redis': 'Redis client',
        'asyncpg': 'PostgreSQL async driver',
        'pydantic': 'Data validation',
        'click': 'CLI framework'
    }
    
    failed = []
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✓ {package:12} - {description}")
        except ImportError:
            print(f"✗ {package:12} - MISSING!")
            failed.append(package)
    
    if failed:
        print(f"\n⚠️  Missing packages: {', '.join(failed)}")
        print("Run: poetry install")
        return False
    
    print("\n✅ All packages installed!")
    return True

def test_env_vars():
    """Test that environment variables are set"""
    
    print("\nTesting environment variables...")
    
    # Load .env file
    from dotenv import load_dotenv
    load_dotenv()
    
    vars_to_check = [
        'OPENAI_API_KEY',
        'ANTHROPIC_API_KEY',
        'DB_PASSWORD',
        'REDIS_PASSWORD'
    ]
    
    missing = []
    for var in vars_to_check:
        value = os.getenv(var)
        if value:
            # Show just first 10 chars for security
            display = value[:10] + "..." if len(value) > 10 else value
            print(f"✓ {var:20} = {display}")
        else:
            print(f"✗ {var:20} - NOT SET!")
            missing.append(var)
    
    if missing:
        print(f"\n⚠️  Missing variables: {', '.join(missing)}")
        print("Check your .env file")
        return False
    
    print("\n✅ All environment variables set!")
    return True

def test_project_structure():
    """Test that all folders exist"""
    
    print("\nTesting project structure...")
    
    folders = [
        'agents', 'core', 'learning', 'data',
        'api', 'cli', 'tests', 'configs',
        'scripts', 'docker', 'venv'
    ]
    
    missing = []
    for folder in folders:
        if os.path.isdir(folder):
            print(f"✓ {folder:12} folder exists")
        else:
            print(f"✗ {folder:12} folder MISSING!")
            missing.append(folder)
    
    if missing:
        print(f"\n⚠️  Missing folders: {', '.join(missing)}")
        return False
    
    print("\n✅ All folders exist!")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("FRACTAL-RMO SETUP TEST")
    print("=" * 50)
    
    # Run all tests
    results = [
        test_project_structure(),
        test_imports(),
        test_env_vars()
    ]
    
    # Final result
    print("\n" + "=" * 50)
    if all(results):
        print("🎉 SETUP COMPLETE! Everything is working!")
        print("\nNext steps:")
        print("1. Start databases: cd docker && docker-compose up -d")
        print("2. Create your first agent in agents/analyzer.py")
        print("3. Run: python test_setup.py")
    else:
        print("⚠️  SETUP INCOMPLETE - Fix the issues above")
        sys.exit(1)
EOF

# Make it executable and run it
chmod +x test_setup.py
python test_setup.py
```

---

## UNDERSTANDING WHAT YOU'VE BUILT

### Project Structure Explained
```
fractal-rmo/
│
├── .env                 # Your secret API keys (NEVER commit this!)
├── .gitignore          # Tells Git what files to ignore
├── pyproject.toml      # Python package requirements
├── poetry.lock         # Exact versions of packages (auto-generated)
├── README.md           # Project description
├── test_setup.py       # Setup verification script
│
├── agents/             # AI agents that do the work
│   ├── __init__.py    # Makes this a Python package
│   └── base_agent.py  # Base class all agents inherit
│
├── docker/            # Database configuration
│   ├── docker-compose.yml  # Docker services config
│   └── init.sql           # Database table creation
│
├── venv/              # Python virtual environment
│   └── (lots of Python files - don't edit these)
│
└── [other folders]    # Ready for your code
```

### How the Pieces Connect
1. **Docker** runs your databases in containers
2. **Python agents** connect to databases to store data
3. **Agents** use AI APIs (OpenAI/Anthropic) to think
4. **Error logs** get stored in PostgreSQL
5. **Patterns** are extracted from errors
6. **Learning** happens by analyzing patterns

---

## COMMON PROBLEMS AND SOLUTIONS

### Problem: "command not found: python3.11"
```bash
# Solution on Mac:
brew install python@3.11

# Solution on Linux:
sudo apt update
sudo apt install python3.11
```

### Problem: "(venv) doesn't appear in prompt"
```bash
# Make sure you're in project folder:
cd ~/CodingProjects/fractal-rmo

# Try activation again:
source venv/bin/activate

# If still not working, recreate venv:
rm -rf venv
python3.11 -m venv venv
source venv/bin/activate
```

### Problem: "Cannot connect to Docker daemon"
```bash
# Make sure Docker Desktop is running
# You should see whale icon in menu bar (Mac)

# Start Docker:
open -a Docker  # On Mac

# Wait 30 seconds for it to start, then retry
```

### Problem: "Poetry: command not found"
```bash
# Make sure venv is active first:
source venv/bin/activate

# Reinstall poetry:
pip install poetry

# Verify:
poetry --version
```

### Problem: Database connection failed
```bash
# Check if containers are running:
docker ps

# If not running, start them:
cd docker
docker-compose up -d

# Check logs for errors:
docker logs fractal_postgres
docker logs fractal_redis
```

---

## STEP 5: CREATE THE ANALYZER AGENT

**What this does**: The Analyzer Agent uses AI to break down big tasks into smaller, manageable pieces called "action items".

```bash
# Navigate to agents folder
cd ~/CodingProjects/fractal-rmo/agents

# Create analyzer.py
cat > analyzer.py << 'EOF'
"""
Analyzer Agent
This agent takes a task description and breaks it down into smaller action items.
It's like a project manager that creates a to-do list from a general goal.
"""

from agents.base_agent import Agent, ActionItem, ExecutionResult
from typing import Dict, List
import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AnalyzerAgent(Agent):
    """Agent that analyzes tasks and creates action items"""
    
    def __init__(self, agent_id: str):
        """Initialize the analyzer with OpenAI client"""
        super().__init__(agent_id, "analyzer")
        
        # Create OpenAI client using your API key
        self.client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
    async def process(self, task: Dict) -> ExecutionResult:
        """Process a task and break it down into action items"""
        
        try:
            # Get the task description from input
            description = task.get('description', '')
            print(f"Analyzing: {description}")
            
            # Ask GPT-4 to break down the task
            response = self.client.chat.completions.create(
                model="gpt-4",  # Using GPT-4 for better analysis
                messages=[
                    {
                        "role": "system", 
                        "content": """You are a task analyzer. Break down the given task into specific action items.
                        Return your response as a JSON array like this:
                        [
                            {"name": "First action", "parameters": {}},
                            {"name": "Second action", "parameters": {}}
                        ]
                        """
                    },
                    {
                        "role": "user", 
                        "content": f"Task: {description}\n\nBreak this into 3-5 specific action items."
                    }
                ],
                temperature=0.3,  # Low temperature = more focused responses
                max_tokens=1000   # Limit response length
            )
            
            # Get the AI's response
            content = response.choices[0].message.content
            print(f"GPT-4 response: {content}")
            
            # Convert response to ActionItem objects
            action_items = self._parse_action_items(content)
            
            # Return successful result
            return ExecutionResult(
                success=True,
                output=action_items,
                tokens_used=response.usage.total_tokens
            )
            
        except Exception as e:
            # If something goes wrong, log it
            print(f"Error in analyzer: {e}")
            self.log_error(e, {"task": task})
            
            return ExecutionResult(
                success=False,
                error=str(e)
            )
    
    def _parse_action_items(self, content: str) -> List[ActionItem]:
        """Convert GPT-4's text response into ActionItem objects"""
        
        try:
            # Try to parse as JSON
            items_data = json.loads(content)
            
            # Convert each item to ActionItem
            items = []
            for i, item in enumerate(items_data):
                action = ActionItem(
                    id=f"action_{i}",
                    name=item.get("name", f"Action {i}"),
                    parameters=item.get("parameters", {})
                )
                items.append(action)
                print(f"Created action: {action.name}")
            
            return items
            
        except json.JSONDecodeError:
            # If JSON parsing fails, create default actions
            print("Could not parse GPT-4 response, using defaults")
            return [
                ActionItem(id="action_1", name="Analyze requirements", parameters={}),
                ActionItem(id="action_2", name="Implement solution", parameters={}),
                ActionItem(id="action_3", name="Validate results", parameters={})
            ]
EOF

echo "Created analyzer.py"
```

---

## STEP 6: CREATE THE VALIDATOR AGENT

**What this does**: The Validator checks if code is correct by parsing it and looking for syntax errors.

```bash
# Still in agents folder
cd ~/CodingProjects/fractal-rmo/agents

# Create validator.py
cat > validator.py << 'EOF'
"""
Validator Agent
This agent checks if code is valid and correct.
It's like a code reviewer that catches errors before they cause problems.
"""

import ast  # Python's Abstract Syntax Tree module for parsing code
from agents.base_agent import Agent, ExecutionResult
from typing import Dict

class ValidatorAgent(Agent):
    """Agent that validates code and results"""
    
    def __init__(self, agent_id: str):
        """Initialize the validator"""
        super().__init__(agent_id, "validator")
        
    async def process(self, task: Dict) -> ExecutionResult:
        """Validate code or other outputs"""
        
        try:
            # Get the code to validate
            code = task.get('code', '')
            
            if not code:
                # No code provided
                return ExecutionResult(
                    success=False,
                    output={"validation": False, "message": "No code provided to validate"}
                )
            
            print(f"Validating code:\n{code[:100]}...")  # Show first 100 chars
            
            # Level 1: Syntax validation
            # Try to parse the code as Python
            try:
                ast.parse(code)
                # If we get here, syntax is valid!
                validation_passed = True
                message = "✓ Syntax validation passed - code is valid Python"
                
            except SyntaxError as e:
                # Syntax error found
                validation_passed = False
                message = f"✗ Syntax error on line {e.lineno}: {e.msg}"
            
            print(message)
            
            # Return validation result
            return ExecutionResult(
                success=validation_passed,
                output={
                    "validation": validation_passed,
                    "message": message,
                    "code_length": len(code),
                    "line_count": len(code.split('\n'))
                }
            )
            
        except Exception as e:
            # Something went wrong during validation
            print(f"Error in validator: {e}")
            self.log_error(e, {"task": task})
            
            return ExecutionResult(
                success=False,
                error=str(e)
            )
EOF

echo "Created validator.py"
```

---

## STEP 7: CREATE THE DATABASE CONNECTION

**What this does**: This code connects your Python application to the PostgreSQL database so you can save and retrieve data.

```bash
# Navigate to data folder
cd ~/CodingProjects/fractal-rmo/data

# Create __init__.py to make it a package
touch __init__.py

# Create database.py
cat > database.py << 'EOF'
"""
Database Connection Manager
This handles all communication with PostgreSQL database.
It's like a translator between Python and the database.
"""

import asyncpg  # Async PostgreSQL driver for Python
import os
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Database:
    """Manages database connections and operations"""
    
    def __init__(self):
        """Initialize database manager"""
        self.pool: Optional[asyncpg.Pool] = None
        
    async def connect(self):
        """Create connection pool to database"""
        
        print("Connecting to PostgreSQL...")
        
        # Create a pool of connections (more efficient than single connection)
        # Pool means multiple operations can happen at once
        self.pool = await asyncpg.create_pool(
            host='localhost',           # Database is on your computer
            port=5432,                  # Standard PostgreSQL port
            user='fractal',             # Username we set up
            password=os.getenv('DB_PASSWORD'),  # Password from .env
            database='fractal_rmo',     # Database name
            min_size=5,                 # Minimum connections to keep open
            max_size=20                 # Maximum connections allowed
        )
        
        print("✓ Connected to PostgreSQL")
    
    async def disconnect(self):
        """Close all database connections"""
        if self.pool:
            await self.pool.close()
            print("Disconnected from PostgreSQL")
    
    async def log_error(self, task_id: str, agent_id: str, 
                       error_type: str, message: str, context: dict):
        """Save an error to the database for learning"""
        
        # Get a connection from the pool
        async with self.pool.acquire() as conn:
            # Insert error into error_logs table
            await conn.execute("""
                INSERT INTO error_logs (task_id, agent_id, error_type, message, context)
                VALUES ($1, $2, $3, $4, $5)
            """, 
            task_id,     # $1
            agent_id,    # $2  
            error_type,  # $3
            message,     # $4
            json.dumps(context)  # $5 - Convert dict to JSON string
            )
            
            print(f"Logged error: {error_type} - {message[:50]}...")
    
    async def create_task(self, description: str) -> str:
        """Create a new task in the database"""
        
        async with self.pool.acquire() as conn:
            # Insert task and return its ID
            task_id = await conn.fetchval("""
                INSERT INTO tasks (description)
                VALUES ($1)
                RETURNING id
            """, description)
            
            print(f"Created task: {task_id}")
            return str(task_id)
    
    async def update_task_status(self, task_id: str, status: str, 
                                 result: Optional[Dict] = None):
        """Update a task's status and results"""
        
        async with self.pool.acquire() as conn:
            # Update the task record
            if result:
                result_json = json.dumps(result)
            else:
                result_json = None
                
            await conn.execute("""
                UPDATE tasks 
                SET status = $1, 
                    result = $2, 
                    completed_at = NOW()
                WHERE id = $3::uuid
            """, status, result_json, task_id)
            
            print(f"Updated task {task_id}: {status}")
    
    async def get_recent_errors(self, limit: int = 10) -> list:
        """Get recent errors for pattern analysis"""
        
        async with self.pool.acquire() as conn:
            # Fetch recent errors
            rows = await conn.fetch("""
                SELECT * FROM error_logs
                ORDER BY time DESC
                LIMIT $1
            """, limit)
            
            # Convert to Python dictionaries
            errors = []
            for row in rows:
                errors.append(dict(row))
            
            return errors

# Create global database instance
# This lets us use 'db' anywhere in the code
db = Database()
EOF

echo "Created database.py"
```

---

## STEP 8: CREATE THE ORCHESTRATOR

**What this does**: The Orchestrator is the conductor - it coordinates all agents to work together on a task.

```bash
# Navigate to core folder
cd ~/CodingProjects/fractal-rmo/core

# Create __init__.py
touch __init__.py

# Create orchestrator.py
cat > orchestrator.py << 'EOF'
"""
Orchestrator
This coordinates all agents to process tasks.
It's like a project manager that assigns work and tracks progress.
"""

import asyncio
from typing import Dict, List
from agents.analyzer import AnalyzerAgent
from agents.validator import ValidatorAgent
from data.database import db

class Orchestrator:
    """Manages the flow of tasks through agents"""
    
    def __init__(self):
        """Initialize with our agents"""
        # Create one instance of each agent type
        self.analyzer = AnalyzerAgent("analyzer_001")
        self.validator = ValidatorAgent("validator_001")
        
    async def process_task(self, description: str) -> Dict:
        """Process a task through the entire pipeline"""
        
        print("\n" + "="*50)
        print(f"PROCESSING TASK: {description}")
        print("="*50)
        
        # Create task in database and get its ID
        task_id = await db.create_task(description)
        
        try:
            # STEP 1: Analyze the task
            print("\n[1/3] Running Analyzer Agent...")
            analysis_result = await self.analyzer.process({
                "description": description
            })
            
            if not analysis_result.success:
                raise Exception(f"Analysis failed: {analysis_result.error}")
            
            # Show what actions were identified
            print(f"Found {len(analysis_result.output)} action items:")
            for item in analysis_result.output:
                print(f"  - {item.name}")
            
            # STEP 2: Execute (simplified for now)
            print("\n[2/3] Executing actions (using sample code)...")
            
            # For proof of concept, we'll use sample code
            # In real system, an Executor agent would generate this
            sample_code = """
def hello_world():
    """A simple function to test validation"""
    print("Hello, World!")
    return True

def calculate_sum(a, b):
    """Add two numbers"""
    return a + b

# Test the functions
if __name__ == "__main__":
    hello_world()
    result = calculate_sum(5, 3)
    print(f"5 + 3 = {result}")
"""
            
            print("Generated sample code:")
            print(sample_code[:200] + "...")
            
            # STEP 3: Validate the code
            print("\n[3/3] Running Validator Agent...")
            validation_result = await self.validator.process({
                "code": sample_code
            })
            
            if validation_result.success:
                print("✅ TASK COMPLETED SUCCESSFULLY!")
                final_status = "completed"
            else:
                print(f"❌ VALIDATION FAILED: {validation_result.output}")
                final_status = "failed"
            
            # Save results to database
            await db.update_task_status(
                task_id,
                final_status,
                {
                    "action_items": [a.__dict__ for a in analysis_result.output],
                    "validation": validation_result.output,
                    "tokens_used": analysis_result.tokens_used
                }
            )
            
            # Return summary
            return {
                "task_id": task_id,
                "success": validation_result.success,
                "action_items": analysis_result.output,
                "validation": validation_result.output,
                "tokens_used": analysis_result.tokens_used,
                "status": final_status
            }
            
        except Exception as e:
            # If anything goes wrong, mark task as failed
            print(f"\n❌ ERROR: {e}")
            
            await db.update_task_status(
                task_id, 
                "failed", 
                {"error": str(e)}
            )
            
            # Log the error for learning
            await db.log_error(
                task_id,
                "orchestrator",
                type(e).__name__,
                str(e),
                {"description": description}
            )
            
            raise e
EOF

echo "Created orchestrator.py"
```

---

## STEP 9: CREATE THE COMMAND-LINE INTERFACE

**What this does**: The CLI lets you interact with your system by typing commands instead of writing code each time.

```bash
# Navigate to cli folder
cd ~/CodingProjects/fractal-rmo/cli

# Create __init__.py
touch __init__.py

# Create main.py
cat > main.py << 'EOF'
"""
Command-Line Interface for Fractal-RMO
This provides commands you can run to interact with the system.
It's like a control panel for your AI agents.
"""

import click  # Library for creating nice CLI commands
import asyncio
from core.orchestrator import Orchestrator
from data.database import db
import json
from datetime import datetime

# Create a group of commands
@click.group()
def cli():
    """Fractal-RMO Command Line Interface
    
    Use these commands to interact with your AI system.
    """
    pass

# Command: process a task
@cli.command()
@click.argument('description')  # Takes the task description as input
def process(description):
    """Process a task through the system
    
    Example: python fractal_rmo.py process "Write a hello world function"
    """
    
    # Define async function to run
    async def run():
        # Connect to database
        await db.connect()
        
        try:
            # Create orchestrator and process the task
            orchestrator = Orchestrator()
            result = await orchestrator.process_task(description)
            
            # Display nice summary
            click.echo("\n" + "="*60)
            click.echo("TASK SUMMARY")
            click.echo("="*60)
            click.echo(f"📋 Task ID: {result['task_id']}")
            
            if result['success']:
                click.echo(f"✅ Status: SUCCESS")
            else:
                click.echo(f"❌ Status: FAILED")
            
            click.echo(f"🤖 Tokens Used: {result['tokens_used']}")
            
            # Estimate cost (rough calculation)
            cost = result['tokens_used'] * 0.00002  # Rough estimate
            click.echo(f"💰 Estimated Cost: ${cost:.4f}")
            
            click.echo(f"\n📝 Action Items Found: {len(result['action_items'])}")
            for item in result['action_items']:
                click.echo(f"   • {item.name}")
            
            if result['validation']:
                click.echo(f"\n✓ Validation: {result['validation']['message']}")
            
            click.echo("="*60)
            
        except Exception as e:
            click.echo(f"\n❌ Task failed: {e}", err=True)
            
        finally:
            # Always disconnect from database
            await db.disconnect()
    
    # Run the async function
    click.echo(f"\n🚀 Starting task: {description}")
    asyncio.run(run())

# Command: test the system
@cli.command()
def test():
    """Test that all components are working"""
    
    async def run_tests():
        click.echo("\n" + "="*60)
        click.echo("SYSTEM TEST")
        click.echo("="*60)
        
        all_good = True
        
        # Test 1: Database connection
        click.echo("\n1. Testing database connection...", nl=False)
        try:
            await db.connect()
            await db.create_task("Test task")
            click.echo(" ✅")
        except Exception as e:
            click.echo(f" ❌ Failed: {e}")
            all_good = False
        
        # Test 2: Analyzer agent
        click.echo("2. Testing Analyzer agent...", nl=False)
        try:
            from agents.analyzer import AnalyzerAgent
            analyzer = AnalyzerAgent("test")
            result = await analyzer.process({
                "description": "Test task"
            })
            if result.success:
                click.echo(" ✅")
            else:
                click.echo(f" ❌ Failed: {result.error}")
                all_good = False
        except Exception as e:
            click.echo(f" ❌ Failed: {e}")
            all_good = False
        
        # Test 3: Validator agent
        click.echo("3. Testing Validator agent...", nl=False)
        try:
            from agents.validator import ValidatorAgent
            validator = ValidatorAgent("test")
            result = await validator.process({
                "code": "print('hello')"
            })
            if result.success:
                click.echo(" ✅")
            else:
                click.echo(f" ❌ Failed: {result.error}")
                all_good = False
        except Exception as e:
            click.echo(f" ❌ Failed: {e}")
            all_good = False
        
        # Test 4: Check Docker containers
        click.echo("4. Checking Docker containers...", nl=False)
        import subprocess
        try:
            result = subprocess.run(
                ["docker", "ps", "--format", "table {{.Names}}"],
                capture_output=True,
                text=True
            )
            if "fractal_postgres" in result.stdout and "fractal_redis" in result.stdout:
                click.echo(" ✅")
            else:
                click.echo(" ❌ Containers not running")
                click.echo("   Run: cd docker && docker-compose up -d")
                all_good = False
        except:
            click.echo(" ❌ Docker not available")
            all_good = False
        
        await db.disconnect()
        
        # Final result
        click.echo("\n" + "="*60)
        if all_good:
            click.echo("✅ ALL TESTS PASSED! System is ready.")
            click.echo("\nTry running a task:")
            click.echo('  python fractal_rmo.py process "Write a Python function"')
        else:
            click.echo("❌ SOME TESTS FAILED. Fix issues above.")
        click.echo("="*60)
    
    # Run tests
    asyncio.run(run_tests())

# Command: show recent errors
@cli.command()
@click.option('--limit', default=5, help='Number of errors to show')
def errors(limit):
    """Show recent errors from the database"""
    
    async def show_errors():
        await db.connect()
        
        errors = await db.get_recent_errors(limit)
        
        if not errors:
            click.echo("No errors found. Good job!")
        else:
            click.echo(f"\nShowing {len(errors)} recent errors:")
            click.echo("="*60)
            
            for i, error in enumerate(errors, 1):
                click.echo(f"\nError {i}:")
                click.echo(f"  Time: {error['time']}")
                click.echo(f"  Type: {error['error_type']}")
                click.echo(f"  Message: {error['message'][:100]}...")
        
        await db.disconnect()
    
    asyncio.run(show_errors())

if __name__ == '__main__':
    cli()
EOF

echo "Created cli/main.py"
```

---

## STEP 10: CREATE THE MAIN ENTRY POINT

**What this does**: This is the main file you'll run to use your system.

```bash
# Go back to project root
cd ~/CodingProjects/fractal-rmo

# Create the main entry point
cat > fractal_rmo.py << 'EOF'
#!/usr/bin/env python3
"""
Fractal-RMO Main Entry Point
Run this file to interact with your AI system.
"""

# Import the CLI commands
from cli.main import cli

if __name__ == '__main__':
    # Run the CLI when this file is executed
    cli()
EOF

# Make it executable
chmod +x fractal_rmo.py

echo "Created fractal_rmo.py"
```

---

## STEP 11: RUN YOUR FIRST TASK!

**Now let's actually use the system you've built!**

```bash
# Make sure you're in the project directory
cd ~/CodingProjects/fractal-rmo

# Activate virtual environment (if not already active)
source venv/bin/activate
# You should see (venv) in your prompt

# Load environment variables
# This makes your API keys available to Python
export $(cat .env | xargs)

# First, test that everything is working
echo "\n🧪 Running system test...\n"
python fractal_rmo.py test

# If all tests pass, you'll see:
# ✅ ALL TESTS PASSED! System is ready.

# If any test fails, fix the issue before continuing
# Common issues:
# - Docker containers not running: cd docker && docker-compose up -d
# - Missing API keys: Check your .env file
# - Database connection failed: Make sure PostgreSQL container is running
```

### Now Process Your First Real Task!

```bash
# Process a simple task
python fractal_rmo.py process "Write a Python function to calculate fibonacci numbers"

# What happens when you run this:
# 1. Task is created in database with unique ID
# 2. Analyzer agent uses GPT-4 to break down the task
# 3. Sample code is generated (simplified for proof of concept)
# 4. Validator checks the code for syntax errors
# 5. Results are saved to database
# 6. Summary is displayed

# Expected output:
# 🚀 Starting task: Write a Python function to calculate fibonacci numbers
# 
# ==================================================
# PROCESSING TASK: Write a Python function to calculate fibonacci numbers
# ==================================================
# 
# [1/3] Running Analyzer Agent...
# Analyzing: Write a Python function to calculate fibonacci numbers
# Found 3 action items:
#   - Define function signature
#   - Implement fibonacci logic
#   - Add test cases
# 
# [2/3] Executing actions (using sample code)...
# Generated sample code...
# 
# [3/3] Running Validator Agent...
# ✓ Syntax validation passed - code is valid Python
# 
# ✅ TASK COMPLETED SUCCESSFULLY!
# 
# ============================================================
# TASK SUMMARY
# ============================================================
# 📋 Task ID: [UUID will appear here]
# ✅ Status: SUCCESS
# 🤖 Tokens Used: ~500
# 💰 Estimated Cost: $0.0100
# 
# 📝 Action Items Found: 3
#    • Define function signature
#    • Implement fibonacci logic  
#    • Add test cases
# 
# ✓ Validation: Syntax validation passed - code is valid Python
# ============================================================
```

### Try More Tasks!

```bash
# Try different task descriptions
python fractal_rmo.py process "Create a web scraper for news articles"

python fractal_rmo.py process "Build a REST API endpoint"

python fractal_rmo.py process "Write unit tests for a calculator class"

# View recent errors (to see the learning data)
python fractal_rmo.py errors --limit 10
```

---

## UNDERSTANDING THE COMPLETE SYSTEM

### How Everything Connects

```
User types command
        ↓
   CLI (main.py)
        ↓
  Orchestrator
        ↓
    Database ← Creates task record
        ↓
  Analyzer Agent
        ↓
    OpenAI API ← Breaks down task
        ↓
  [Executor Agent - placeholder for now]
        ↓
  Validator Agent ← Checks code
        ↓
    Database ← Saves results
        ↓
  CLI displays summary
```

### What Each File Does

- **fractal_rmo.py**: Main entry point - run this to use the system
- **cli/main.py**: Command definitions - what happens when you type commands
- **core/orchestrator.py**: Coordinates agents - manages the workflow
- **agents/analyzer.py**: Uses AI to break down tasks
- **agents/validator.py**: Checks if code is correct
- **data/database.py**: Saves everything to PostgreSQL
- **docker/**: Runs your databases in containers
- **.env**: Stores your secret API keys

### Next Development Steps

1. **Add Executor Agent** (Next Day)
   - Actually generates code instead of using samples
   - Uses GPT-4 or Claude to write real functions

2. **Add Pattern Extraction** (Week 2)
   - Analyzes errors to find patterns
   - Creates learning/pattern_extractor.py

3. **Implement Learning Loop** (Week 3)
   - Updates agent behavior based on patterns
   - Measures improvement over time

4. **Add More Validators** (Week 4)
   - Static analysis with pylint
   - Unit test execution
   - Performance benchmarks

5. **Build Web API** (Month 2)
   - REST API with FastAPI
   - Web interface for easier use

---

## QUICK REFERENCE - COMMANDS YOU'LL USE OFTEN

```bash
# Navigate to project
cd ~/CodingProjects/fractal-rmo

# Activate virtual environment
source venv/bin/activate

# Start databases
cd docker && docker-compose up -d

# Stop databases
cd docker && docker-compose down

# View database logs
docker logs fractal_postgres
docker logs fractal_redis

# Install a new package
poetry add package_name

# Run tests
pytest

# Check what's running
docker ps

# Git commands
git status          # See what changed
git add .           # Stage all changes
git commit -m "Message"  # Save changes
git log --oneline   # See history
```

---

This guide should get you from zero to a working foundation. Each command is explained, each concept is clear. You're ready to build Fractal-RMO!
