# 🎯 PROJECT OVERVIEW - CURRENT STATE
## Living Snapshot of Fractal-RMO Development

[Last Updated: 2025-08-31 | 13:55 EST | By: Claude-4.1-Opus]

======================================================================
======================================================================


# PROJECT DESCRIPTION & MECHANICS
**[Permanent Section - Update Only When Core Mission Changes]**

## What Is Fractal-RMO?

**PROJECT:** Fractal-RMO (Recursive Multi-Objective Learning System)

**PURPOSE:** Detect, analyze, and learn from LLM failure patterns to systematically improve agent performance across all domains

**CURRENT STAGE:** Proof of Concept Development

**CHRIS'S VISION:** "I quit my job to build this masterpiece framework" - Building genuinely novel error attribution that makes LLMs learn from their fuck-ups

## How The System Actually Works:

**THE PROCESS:**
1. **RECORD** - Every agent action gets logged with full context
2. **DETECT** - System identifies when agents fail or produce errors  
3. **ANALYZE** - ML algorithms find patterns in the failures
4. **SIGNATURE** - Create unique "fingerprints" for each error type
5. **LEARN** - Build a knowledge base of failure patterns
6. **PREVENT** - Train agents to recognize and avoid these patterns
7. **ITERATE** - System gets smarter with each error encountered

**KEY COMPONENTS:**
• **Agents** - Multiple specialized LLMs doing different tasks
• **Orchestrator** - Coordinates agents and routes tasks
• **Error Logger** - Captures all failures with context
• **Pattern Detector** - ML system finding failure commonalities
• **Learning Module** - Builds error avoidance strategies
• **Validation System** - Tests if errors are actually fixed

**WHY IT'S REVOLUTIONARY:**
- Current LLMs repeat the same mistakes forever
- Fractal-RMO creates a "memory" of what doesn't work
- Cross-domain learning means fixing an error in one area helps ALL areas
- Systematic improvement instead of random prompt engineering


======================================================================
======================================================================








# TECHNICAL SETUP
**[Version 1 - Created 2025-08-31 | Update When Architecture Changes]**

## Current Dependencies & Infrastructure:

### 🐍 Python Environment:
- **Version:** Python 3.13.7
- **Virtual Environment:** `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/11--(Python)_(Virtual)_(Environment)/venv/`
- **Package Manager:** Poetry 2.1.4
- **Activation:** `source 11--(Python)_(Virtual)_(Environment)/venv/bin/activate`

### 🐳 Docker Databases:
- **PostgreSQL:** Port 5432 (Container: fractal_postgres)
- **Redis:** Port 6379 (Container: fractal_redis)
- **Config Location:** `./10--(Docker)_(Database)_(Setup)/`
- **Status:** ✅ Running and healthy

### 📦 Key Installed Packages:
- **Web:** FastAPI, Uvicorn
- **Database:** AsyncPG 0.30.0, SQLAlchemy, Redis
- **AI:** OpenAI, Anthropic libraries
- **ML:** NumPy, Scikit-learn
- **Dev:** pytest, black, pylint

### 🔑 Configuration Files:
- **.env:** API keys and passwords (NEEDS REAL KEYS ADDED)
- **pyproject.toml:** Dependency definitions
- **.gitignore:** Prevents sensitive file commits

## Version Change Log:
- v1: Initial setup with Python 3.13.7, asyncpg 0.30.0 for compatibility


======================================================================
======================================================================








# CURRENT WORK CONTEXT
**[Update EVERY Session]**

## 📂 Active Work Documentation:

**PRIMARY WORK FILE:** `2--(Documentation)_(Update)_(Fixes)`
- Full path: `./12--(Progress)_(Tracking)_(What)_(We)_(Did)/2--(Documentation)_(Update)_(Fixes)/`

**ADDITIONAL CONTEXT NEEDED:** None currently

**CURRENT PHASE:** Fixed documentation update prompt with correct paths and rules

**NEXT PLANNED WORK:** Create base agent Python files in `1--(AI)_(Agents)/` folder


======================================================================
======================================================================








# SHORT-TERM MEMORY
**[Rolling - Keep Latest 3 Entries, Delete Oldest When Adding 4th]**

## Recent Work Sessions:

### 📍 Entry 3 (Latest):
[2025-08-31 | 12:29-13:55 EST | Claude-4.1-Opus]
**WHAT:** Fixed all documentation issues and changed timezone to EST
**WHERE:** `./12--(Progress)_(Tracking)_(What)_(We)_(Did)/` contribution guidelines and prompts
**RESULT:** Added Session Insights rules, header timestamp rule, fixed all PST→EST
**NEXT:** Create base agent Python files in `1--(AI)_(Agents)/`

### 📍 Entry 2:
[2025-08-31 | 12:29-13:31 EST | Claude-4.1-Opus]
**WHAT:** Fixed broken documentation update prompt with correct paths
**WHERE:** `./12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.5--(Documentation)_(Update)_(Prompt)/`
**RESULT:** Replaced wrong file paths, fixed memory entry order, updated validator location
**KEY INSIGHT:** Previous agent lost context and created unusable prompt

### 📍 Entry 1:
[2025-08-31 | 07:00-07:45 EST | Claude-3.5]
**WHAT:** Complete rewrite of documentation system with strict rules
**WHERE:** `./12--(Progress)_(Tracking)_(What)_(We)_(Did)/` all files
**RESULT:** Numbered rules (§1.1 format), exact templates, validator script created
**KEY INSIGHT:** LLMs need exact templates and rules, not general guidance


======================================================================
======================================================================








# SESSION INSIGHTS
**[Sticky Notes - Important Realizations/Decisions]**

💡 **venv in numbered folder breaks some tools**
- Located at `./11--(Python)_(Virtual)_(Environment)/venv/` not project root
- Some tools expect venv at project root and fail

💡 **Python 3.13 breaks many packages**
- asyncpg 0.28.0 wouldn't compile, needed 0.30.0
- Check compatibility before using bleeding-edge Python

💡 **Agent context loss creates broken references**
- Previous agent created prompt with non-existent file paths
- Always verify file paths exist before referencing them

💡 **Documentation validator path moved**
- Was at `9--(Helper)_(Scripts)/` 
- Now at `12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/`


======================================================================
======================================================================








# QUICK STATUS CHECK
**[For Chris's ADHD - The TL;DR]**

✅ **DONE:** Environment fully set up - Python, Docker, all dependencies

🔨 **DOING:** Created documentation system, ready for agent coding

🎯 **NEXT:** Write Python code for base agents in `1--(AI)_(Agents)/`

⚠️ **BLOCKED:** Need real API keys in .env file (OpenAI and Anthropic)

📝 **TO REMEMBER:** 
- Docker databases are running (don't forget they're there)
- venv is in the numbered folder (non-standard location)
- Use the contribution guidelines for all documentation


======================================================================
======================================================================
