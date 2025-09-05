# TRUNK-BRANCH DOCUMENTATION SYSTEM - COMPLETE STRUCTURE
## Exhaustive Directory Layout and Naming Conventions

[Created: 2025-09-01 | 03:46 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 04:25 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 09:00 EST | By: Claude-4.1-Opus | Major updates: folder rename, master timestamp log, sub-branch propositions]
[Revised: 2025-09-01 | 20:35 EST | By: Claude-4.1-Opus | Fixed: folder naming with underscores, clarified system design]
[Revised: 2025-09-03 | 10:20 EST | By: Claude-4.1-Opus | Added: How Context Analysis uses structure]
[Document 2 of 4 in Trunk-Branch System Documentation]


------------------------------------------------------

## What The Fuck Is This?

This document shows EXACTLY where every file lives in the trunk-branch system, how to name everything, and the complete folder hierarchy.

• **No ambiguity** - Every path is explicit
• **Visual diagrams** - See the structure at a glance  
• **Naming rules** - Know exactly what to call things


------------------------------------------------------

## Master Directory Structure

```
12--(Progress)_(Tracking)_(What)_(We)_(Did)/
│
├── 0--(README_Folder)/
│   └── (README_Folder).md
│
├── 0.1--(Contribution)_(Guidelines)_(MUST_READ)/
│   └── (Contribution)_(Guidelines)_(MUST_READ).md
│
├── 0.2--(Trunk)_(Branch)_(System)/           [Main documentation system folder]
│   ├── 0--(README_Folder)/
│   │   └── (README_Folder).md
│   │
│   ├── 0.1--(Index)_(Main_Bnchs)/           [Index of MAIN branches]
│   │   └── (Index)_(Main_Bnchs).md
│   │
│   ├── 0.2--(Master)_(Timestamp)_(Log)/     [⚠️ DEPRECATED - Git replaced this]
│   │   └── (Master)_(Timestamp)_(Log).md    [No longer used - Git tracks all timestamps]
│   │
│   ├── 0.3--(LLM)_(Limitations)_(Discovered)/  [Project-wide LLM failure patterns]
│   │   └── (LLM)_(Limitations)_(Discovered).md
│   │
│   ├── 1--(Trunk)_(O-F)/                    [The trunk overview]
│   │   └── (Trunk)_(O-F).md
│   │
│   ├── 2--(A)_(Main_Bnch)_(O-F)/            [Main branch A]
│   │   ├── 0--(README_Folder)/              [Explains branch contents]
│   │   │   └── (README_Folder).md
│   │   │
│   │   ├── 0.1--(Index)_(Sub-Bnchs)/        [Lists A's sub-branches]
│   │   │   └── (Index)_(Sub-Bnchs).md
│   │   │
│   │   ├── 0.2--(Sub-Bnch)_(Propositions)/   [NEW: Proposed sub-branches]
│   │   │   └── (Sub-Bnch)_(Propositions).md
│   │   │
│   │   ├── 1--(A)_(Main_Bnch)_(O-F)/        [A's main overview]
│   │   │   └── (A)_(Main_Bnch)_(O-F).md
│   │   │
│   │   ├── 2--(A-1)_(Sub_Bnch)_(O-F)/       [Sub-branch A-1]
│   │   │   ├── (A-1)_(Sub_Bnch)_(O-F).md
│   │   │   ├── (A-1)_(Work)_(History)_(Index).md [5-7 word summaries!]
│   │   ├── (A-1)_(Handoff)_(Status).md  [Minimal with new O-F]
│   │   │   ├── 1--(A-1)_(Setup)_(Initial)/
│   │   │   │   └── (A-1)_(Setup)_(Initial).md
│   │   │   └── 2--(A-1)_(Implementation)_(Core)/
│   │   │       └── (A-1)_(Implementation)_(Core).md
│   │   │
│   │   └── 3--(A-2)_(Sub_Bnch)_(O-F)/       [Sub-branch A-2]
│   │       ├── (A-2)_(Sub_Bnch)_(O-F).md
│   │       ├── (A-2)_(Work)_(History)_(Index).md
│       ├── (A-2)_(Handoff)_(Status).md  [Minimal with new O-F]
│   │       └── [Work history files...]
│   │
│   ├── 3--(B)_(Main_Bnch)_(O-F)/            [Main branch B]
│   │   └── [Same structure as A...]
│   │
│   └── 4--(C)_(Main_Bnch)_(O-F)/            [Main branch C]
│       └── [Same structure as A...]
│
├── 0.3--(LLM)_(Limitations)_(Discovered)/    [MOVED: Now inside trunk system]
│   └── [This folder deprecated - see 0.2 trunk system]
│
├── 0.4--(Documentation)_(Validator)_(Script)_(BS)/
│   └── session_end_validator.py [Chris says this is "bullshit" - needs rewrite]
│
└── 0.5--(Documentation)_(Update)_(Prompt)/
    └── (Documentation)_(Update)_(Prompt).md
```

**WHY This Structure?**

• **0.2-- position for timestamp log:** Chris specifically said "just after the main branch's 0--(README_Folder), and 0.1--(Index)_(Sub-Bnchs) folders" - this placement ensures consistent ordering

• **Work history indexes in sub-branches:** These contain 5-7 word summaries of each work file so agents can quickly find specific work without reading everything

• **Numbered folders:** Enable clear hierarchy and prevent naming conflicts


------------------------------------------------------

## Naming Convention Rules

### Overview Files (O-F)

**Trunk O-F:**
```
Filename: (Trunk)_(O-F).md
Path: 0.2--(Trunk)_(Branch)_(System)/1--(Trunk)_(O-F)/(Trunk)_(O-F).md
```

**Main Branch O-F:**
```
Pattern: (LETTER)_(Main_Bnch)_(O-F).md
Example: (A)_(Main_Bnch)_(O-F).md
Example: (B)_(Main_Bnch)_(O-F).md
```

**Sub-Branch O-F:**
```
Pattern: (LETTER-NUMBER)_(Sub_Bnch)_(O-F).md
Example: (A-1)_(Sub_Bnch)_(O-F).md
Example: (B-3)_(Sub_Bnch)_(O-F).md
```

**Merged Branch O-F:**
```
Pattern: (LETTER-LETTER)_(Main_Bnch)_(O-F).md
Example: (C-F)_(Main_Bnch)_(O-F).md
Note: Original C and F branches remain intact
```


------------------------------------------------------

## THE NEW TASK-BASED O-F STRUCTURE (CRITICAL - THIS IS THE STANDARD)

### The Revolution in Sub-Branch Documentation

**THE PROBLEM:** Old O-F structure gave agents no real context - just 3 recent items and vague status
**THE SOLUTION:** Task-based structure that serves as complete project management AND context system

### The NEW Standard Sub-Branch O-F Format:

```markdown
# (A-1)_(Sub_Bnch)_(O-F).md

## DELIVERABLE DEFINITION
[One clear sentence defining what this sub-branch produces]
Example: "Build base agent classes with OpenAI and Anthropic support"

## MASTER TASK BREAKDOWN

### Task 1: [Major Component] [✅ COMPLETE or ⚠️ IN PROGRESS or 📋 PLANNED]
**Sub-tasks:**
- 1.1 [Specific implementation] [✅ or 🔄 CURRENT or 📋]
  Summary: [What was built/decided if complete]
  Insight: 💡 [Any gotcha or important discovery]
- 1.2 [Another sub-task] [Status]
  Summary: [Brief outcome if complete]

### Task 2: [Next Major Component] [Status]
**Sub-tasks:**
- 2.1 [Implementation detail] [Status]
  Summary: [Outcome]
- 2.2 [Another detail] [Status]

### Task 3: [Another Component] [Status]
**Sub-tasks:**
[Continue pattern...]

## DEPENDENCY CHAIN
Direct dependencies: [Which branches this needs]
[Branch] depends on: [Its dependencies]
Full chain: [Complete dependency tree]
Last sync commit: [Git commit hash when last checked dependencies]

## SHARED CONTEXT SOURCES
- [Branch-ID]: [What was imported] [Date/Time]
  * [How it's being used]
  * [Any adaptations made]

## SHORT-TERM MEMORY (Recent Work)
Entry 3: [Most recent work item]
Entry 2: [Previous work]
Entry 1: [Older work]
```

### Real Example of Task-Based O-F:

```markdown
# (A-1)_(Sub_Bnch)_(O-F).md

## DELIVERABLE DEFINITION
Build base agent classes with OpenAI and Anthropic support

## MASTER TASK BREAKDOWN

### Task 1: Environment Setup ✅ COMPLETE
**Sub-tasks:**
- 1.1 Virtual environment creation ✅
  Summary: Python 3.12 venv with Poetry
- 1.2 Dependency installation ✅
  Summary: OpenAI, Anthropic, asyncio packages
  Insight: 💡 Python 3.13 breaks asyncio - stick to 3.12
- 1.3 Project structure ✅
  Summary: Created agents/, tests/, configs/ folders

### Task 2: Base Agent Class ⚠️ IN PROGRESS
**Sub-tasks:**
- 2.1 Abstract base class ✅
  Summary: Created BaseAgent with required methods
- 2.2 OpenAI implementation ✅
  Summary: Subclass with GPT-4 integration
  Insight: 💡 Rate limiting at 10 req/min on free tier
- 2.3 Anthropic implementation 🔄 CURRENT
  Notes: Working on Claude integration
- 2.4 Error handling patterns 📋 PLANNED
- 2.5 Async/await structure 📋 PLANNED

### Task 3: Testing Framework 📋 PLANNED
**Sub-tasks:**
- 3.1 Unit test structure
- 3.2 Mock LLM responses
- 3.3 Integration tests

## DEPENDENCY CHAIN
Direct dependencies: B-3 (auth patterns)
B-3 depends on: C-1 (database)
Full chain: A-1 → B-3 → C-1
Last sync commit: abc123def

## SHARED CONTEXT SOURCES
- B-3: OAuth2 patterns [2025-09-01 | 14:00 EST]
  * Using token refresh approach
  * Adapted error types to AgentError

## SHORT-TERM MEMORY
Entry 3: Debugging Anthropic API connection
Entry 2: Added retry decorator from B-3
Entry 1: Fixed async context manager issue
```

### Why This Structure is Revolutionary:

**Solves Context Engineering Gap:**
• Agents see EXACTLY what the deliverable is
• Complete roadmap of all work (past and future)
• Current position clearly marked (🔄 CURRENT)
• Insights attached to relevant tasks, not floating
• Dependencies tracked with Git commit hashes

**Three Birds with One Stone:**
1. **Long-term memory** - The task list IS the memory
2. **Current position** - See exactly where we are
3. **Context at right level** - Summaries where needed

**Impact on Other Files:**
• **Handoff files become minimal** - Just point to current task position
• **Work History still valuable** - For deep dives into specific implementations
• **O-F becomes single source of truth** - Everything important is here

**Chris's Vision Realized:**
> "This might negate what's needed in the Handoff file in general"

Exactly right - the comprehensive task structure means handoffs just say "I'm at Task 2.3, blocked on X"


------------------------------------------------------

## Branch Naming System

### Main Branches

**Assignment Rules:**
• Use single letters: A, B, C, D, etc.
• Sequential assignment
• Never reuse letters (even if branch completes)

**Examples:**
```
A = Agent System
B = API Development  
C = Orchestrator
D = Database Layer
E = Error Detection
```


### Sub-Branches

**Assignment Rules:**
• Parent letter + dash + number
• Numbers start at 1 for each main branch
• Sequential within branch

**Examples:**
```
A-1 = Base agent creation
A-2 = Agent error handling
A-3 = Agent routing

B-1 = Authentication endpoints
B-2 = Data endpoints
B-3 = Admin endpoints
```


------------------------------------------------------

## Work History Organization

### Sub-Branch Work History

**Location:** Inside each sub-branch folder
```
2--(A-1)_(Sub_Bnch)_(O-F)/
├── (A-1)_(Sub_Bnch)_(O-F).md             [Now contains task-based structure - THE source of truth]
├── (A-1)_(Work)_(History)_(Index).md     [CRITICAL: 5-7 word summaries!]
├── (A-1)_(Handoff)_(Status).md          [MINIMAL - just points to current task in O-F]
├── 1--(A-1)_(Setup)_(Initial)/           [Work history 1 - EXAMPLE NAME]
│   └── (A-1)_(Setup)_(Initial).md
├── 2--(A-1)_(Implementation)_(Core)/     [Work history 2 - EXAMPLE NAME]
│   └── (A-1)_(Implementation)_(Core).md
└── 3--(A-1)_(Testing)_(Validation)/      [Work history 3 - EXAMPLE NAME]
    └── (A-1)_(Testing)_(Validation).md
```

**Note:** Work history folder names are EXAMPLES - use descriptive names for actual work

**CORRECT Index Format (5-7 Word Summaries):**
```markdown
# Work History Index - Branch A-1
[Last Updated: 2025-09-01 | 15:00 EST]

## Work History Files:
1. **Setup Initial** - Environment config and dependency installation
2. **Implementation Core** - Built base agent class methods
3. **Testing Validation** - Created unit tests fixed bugs
```

**WHY 5-7 words?**
Chris specified: "receive only the titles and maybe like a 5-7 word-ish summary" - this keeps indexes scannable while providing enough context to find specific work.

**Note:** With new task-based O-F structure, agents primarily get context from O-F task breakdown, using work history only for deep dives into specific implementations.

**WRONG Index Format (Too detailed):**
```markdown
1. **Setup Initial** - This file contains all the environment configuration including Python virtual environment setup, dependency installation via Poetry, Docker configuration... [NO! Too long!]
```

### Index Hierarchy Explained

**Three Levels of Indexes:**

1. **Trunk Level:** Lists all main branches
   ```
   Path: 0.2--(Trunk)_(Branch)_(System)/0.1--(Index)_(Main_Bnchs)/
   Content: Lists A, B, C main branches
   ```

2. **Main Branch Level:** Lists its sub-branches
   ```
   Path: 2--(A)_(Main_Bnch)_(O-F)/0.1--(Index)_(Sub-Bnchs)/
   Content: Lists A-1, A-2, A-3 sub-branches
   ```

3. **Sub-Branch Level:** Lists work history files
   ```
   Path: 2--(A-1)_(Sub_Bnch)_(O-F)/(A-1)_(Work)_(History)_(Index).md
   Content: 5-7 word summaries of each work file
   ```

**Chris's specification:** "Main branch should just get an index of the sub branches, and the sub branches get an index of the work history files"


------------------------------------------------------

## Special Files and Logs

### Master Timestamp Log (DEPRECATED)

**Status:** DEPRECATED as of 2025-09-04
**Replaced by:** Git commit history

**Old Purpose:** Single source of truth for ALL sub-branch update times
**New System:** Git tracks all updates via commit history

**Each O-F file now stores:**
• Last sync commit: [git commit hash]

**To check updates:**
• Use: `git log --grep="O-F" --oneline`
• Not: Master Timestamp Log

**Migration:**
• Existing timestamp log can be deleted after migration
• All timestamp tracking now through Git commits

**NOTE:** Individual branch timestamp logs at 0.2 position REMOVED. All timestamps now tracked via Git commits. No branch-specific timestamp files needed.


### Branch Index Files

**Trunk Level Index:**
```
Path: 0.2--(Trunk)_(Branch)_(System)/0.1--(Index)_(Main_Bnchs)/(Index)_(Main_Bnchs).md

Content:
# Master Branch Index

## Main Branches:
- A: Agent System (Active)
- B: API Development (Active)
- C: Orchestrator (Planned)

## Merged Branches:
- C-F: Combined Cache-Frontend (Active)
```

**Main Branch Level Index:**
```
Path: 2--(A)_(Main_Bnch)_(O-F)/0.1--(Index)_(Sub-Bnchs)/

Content:
# Branch A Sub-Branch Index

## Sub-Branches:
- A-1: Base Agent Creation (Complete)
- A-2: Error Handling (Active)
- A-3: Agent Routing (Planned)
```


------------------------------------------------------

## Context Sharing File References

### When A-1 Needs Context from B-3

**In A-1's O-F file:**
```markdown
## Shared Context Sources:
- B-3: Authentication logic [Timestamp: 2025-09-01 | 10:00 EST]
- C-4: Database connections [Timestamp: 2025-09-01 | 09:30 EST]
- D: Complete error handling patterns [Timestamp: 2025-09-01 | 08:00 EST]
- Last sync commit: abc123def  [← ADD THIS LINE]
```

**Update checking:**
A-1 no longer checks Master Timestamp Log
Instead uses: `git diff [last-sync-commit] HEAD -- "B-3_folder/"`


------------------------------------------------------

## README Requirements

### Every Folder With 2+ Items Needs:
```
0--(README_Folder)/(README_Folder).md
```

**Required READMEs:**
• `0.2--(Trunk)_(Branch)_(System)/0--(README_Folder)/`
• Each main branch folder
• Any sub-branch with multiple work history files


------------------------------------------------------

## File Path Examples

### Complete Paths for Common Files:

**Trunk O-F:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/
12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Trunk)_(Branch)_(System)/1--(Trunk)_(O-F)/(Trunk)_(O-F).md
```

**Branch A Main O-F:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/
12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Trunk)_(Branch)_(System)/2--(A)_(Main_Bnch)_(O-F)/
1--(A)_(Main_Bnch)_(O-F)/(A)_(Main_Bnch)_(O-F).md
```

**Sub-Branch A-1 O-F:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/
12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Trunk)_(Branch)_(System)/2--(A)_(Main_Bnch)_(O-F)/
2--(A-1)_(Sub_Bnch)_(O-F)/(A-1)_(Sub_Bnch)_(O-F).md
```

**A-1 Work History:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/
12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Trunk)_(Branch)_(System)/2--(A)_(Main_Bnch)_(O-F)/
2--(A-1)_(Sub_Bnch)_(O-F)/1--(A-1)_(Setup)_(Initial)/(A-1)_(Setup)_(Initial).md
```


------------------------------------------------------

## Migration from Current Structure

### Current → New Mapping:

**Current:**
```
0.2--(Project)_(Overview)_(Current)_(State)/
└── (Project)_(Overview)_(Current)_(State).md
```

**Becomes:**
```
0.2--(Trunk)_(Branch)_(System)/
├── 1--(Trunk)_(O-F)/
│   └── (Trunk)_(O-F).md  [Modified version of current]
```

**Current work files:**
```
1--(PoC)_(Project)_(Setup)/
2--(Documentation)_(Update)_(Fixes)/
```

**Become sub-branches:**
```
2--(A)_(Main_Bnch)_(O-F)/  [Project Setup Branch]
├── 2--(A-1)_(Sub_Bnch)_(O-F)/  [Environment setup]
└── 3--(A-2)_(Sub_Bnch)_(O-F)/  [Documentation fixes]
```


------------------------------------------------------

## Directory Creation Commands

### To Create Branch A Structure:
```bash
# From 0.2--(Trunk)_(Branch)_(System)/ directory
mkdir -p "2--(A)_(Main_Bnch)_(O-F)/0--(README_Folder)"
mkdir -p "2--(A)_(Main_Bnch)_(O-F)/0.1--(Index)_(Sub-Bnchs)"
mkdir -p "2--(A)_(Main_Bnch)_(O-F)/0.2--(Sub-Bnch)_(Propositions)"
mkdir -p "2--(A)_(Main_Bnch)_(O-F)/1--(A)_(Main_Bnch)_(O-F)"
mkdir -p "2--(A)_(Main_Bnch)_(O-F)/2--(A-1)_(Sub_Bnch)_(O-F)"
# NOTE: No timestamp log folder - Git commit history handles all timestamp tracking
```


------------------------------------------------------

## Validation Rules

### Valid Structure Checks:

✓ **Every main branch has:**
• 0--(README_Folder)
• 0.1--(Index)_(Sub-Bnchs)
• 0.2--(Sub-Bnch)_(Propositions)  [NEW - replaces timestamp logs]
• 1--(X)_(Main_Bnch)_(O-F)

✅ **Every sub-branch has:**
• (X-N)_(Sub_Bnch)_(O-F).md file
• (X-N)_(Work)_(History)_(Index).md if has work history

✅ **Naming follows pattern:**
• Main branches: Single letter
• Sub-branches: Letter-Number
• All use underscores and parentheses


------------------------------------------------------

## How Context Analysis Uses This Structure

### The Scanning Process

**When agents run Context Analysis Protocol, they navigate:**

1. **Start at Main Branch Index**
   ```
   Path: 0.1--(Index)_(Main_Bnchs)/(Index)_(Main_Bnchs).md
   Purpose: Quick overview of all domains
   Example: "A = Agent System, B = API, C = Database"
   ```

2. **Check Sub-Branch Indexes for relevant branches**
   ```
   Path: [Branch]/0.1--(Index)_(Sub-Bnchs)/(Index)_(Sub-Bnchs).md
   Purpose: See what deliverables exist in each domain
   Example: "A-1: Base agents (Complete), A-2: Error handling (Active)"
   ```

3. **Scan Work History Indexes for specifics**
   ```
   Path: [Sub-Branch]/(X-N)_(Work)_(History)_(Index).md
   Purpose: 5-7 word summaries reveal what's been built
   Example: "3. Testing Validation - Created unit tests fixed bugs"
   ```

4. **Only read full O-F files for RELEVANT branches**
   ```
   Don't waste time reading everything
   Indexes give targeting information
   Read details only after marking RELEVANT
   ```

### Prerequisites and Propositions

**When Gate 0 triggers (missing prerequisites):**

1. **Check Proposition Sheets first**
   ```
   Path: [Main_Branch]/0.2--(Sub-Bnch)_(Propositions)/(Sub-Bnch)_(Propositions).md
   Why: Someone might have already proposed what you need
   Status check: PROPOSED, APPROVED, REJECTED, CREATED
   ```

2. **If not proposed, add your proposition**
   ```
   Add to the SINGLE propositions file (not separate files)
   Include: What's needed, why, deliverable description
   Flag for Chris review
   ```

### Master Timestamp Log for Dependencies

**Critical for lazy updates:**
```
Path: 0.2--(Master)_(Timestamp)_(Log)/(Master)_(Timestamp)_(Log).md
Use: Check when ANY sub-branch last updated
Format: Alphanumerical list with timestamps
Purpose: Detect stale dependencies without reading everything
```

### Context Documentation Location

**Where context imports get recorded:**
```
In each Sub-Branch O-F:
  ## Shared Context Sources:
  - Lists what was imported
  - When it was imported (timestamp)
  - Why it was needed
  - What was extracted vs ignored

In Handoff Files:
  ## Dependencies:
  - Current import status
  - What needs updating
  - Blocking dependencies
```

### The Efficiency Pattern

**Why this structure enables fast context analysis:**

1. **Indexes prevent reading everything**
   • Main index: 30 seconds to scan all branches
   • Sub indexes: Find relevant work instantly
   • Work indexes: 5-7 word summaries = quick targeting

2. **Propositions prevent duplicate work**
   • See what's already planned
   • Avoid creating redundant branches
   • Track approval status

3. **Master timestamp enables lazy updates**
   • One file shows all update times
   • Quick staleness detection
   • No cascading reads needed

4. **O-F files contain extraction details**
   • What to take from each import
   • Clear documentation trail
   • No guesswork needed


------------------------------------------------------

## 🔔 PENCILED ITEMS - Structure Decisions

### Maximum Branch Depth
**RESOLVED (2025-09-01):** Two levels only (Main → Sub)
• No sub-sub-branches (no A-1-a)
• Keeps structure simple and scannable
• If sub-branch gets complex, create new sub-branch instead

### Branch Archival
**What needs deciding:** Where do completed branches go?
**Options:** Archive folder vs keeping in place with status marker
**Consideration:** Need to preserve work history

### Cross-Project Branches
**What needs deciding:** Can branches span multiple PoC folders?
**Context:** If agent work touches multiple system parts
**Current thought:** Keep branches within single PoC folder


------------------------------------------------------

## Why This Document Matters

Without exact paths and naming conventions, agents will create chaos. This document is the map - every file has one correct location and name.

Next document explains HOW agents work within this structure.


======================================================================
======================================================================
