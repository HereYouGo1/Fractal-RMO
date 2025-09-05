# TRUNK-BRANCH DOCUMENTATION SYSTEM - OPERATIONS MANUAL
## Complete Agent Workflows and Update Procedures

[Created: 2025-09-01 | 03:48 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 04:30 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 09:30 EST | By: Claude-4.1-Opus | Major updates: master timestamp log, dependency chains, deliverable-based branches]
[Revised: 2025-09-01 | 20:40 EST | By: Claude-4.1-Opus | Fixed: clarified system design, proper documentation protocol]
[Revised: 2025-09-03 | 10:25 EST | By: Claude-4.1-Opus | Added: Complete Context Analysis Guidelines]
[Document 3 of 4 in Trunk-Branch System Documentation]


------------------------------------------------------

## What The Fuck Is This?

This document explains EXACTLY how agents work within the trunk-branch system - from login to logout, including all update procedures, branch creation, and synchronization.

• **Step-by-step workflows** - No ambiguity about what to do
• **Common scenarios** - See exactly how things work in practice
• **Update cascading** - Understand what updates where and when


------------------------------------------------------

## Agent Login Procedure

### Step 1: Initial Context Load

**Agent receives:**
```
1. Personality documents (Chris's style guide)
2. File naming conventions
3. Contribution guidelines (updated for trunk-branch)
4. Trunk O-F file
5. Branch assignment (e.g., "You're working on A-1")
```

### Step 2: Dependency Chain Check

**Agent checks Git for dependency updates:**
```bash
# Check when dependencies last updated
git log --grep="O-F" --oneline --since="last-sync"
```

**WHY this matters:**
Git commit history tells you when EVERY sub-branch last updated. Without checking this, you might work with outdated context and create inconsistencies.

**Agent checks dependency chain:**
If working on E-7, check its O-F file (O-F = Overview File - the main documentation for each branch):
```markdown
## Dependency Chain:
Direct dependencies: A-6
A-6 depends on: C-4
Full chain: E-7 → A-6 → C-4
```

**Agent compares timestamps:**
• E-7 last synced with A-6: 12:00 EST (from E-7's O-F)
• A-6 last updated: 12:00 EST (from master log)
• C-4 last updated: 17:00 EST (from master log)
• **PROBLEM:** C-4 updated AFTER A-6's last sync!

### Step 3: Blocked or Proceed Decision

**If dependencies are outdated (like E-7 example above):**
```
🔴 STARTUP BLOCKED - Dependency Chain Issue

E-7 cannot proceed because:
• E-7 depends on A-6 (last synced: 12:00 EST)
• A-6 depends on C-4 (updated: 17:00 EST) 
• A-6 needs update from C-4 first

To resolve:
1. Run update agent on A-6, or
2. Manually update A-6 with C-4's context

Current chain: E-7 → A-6 [OUTDATED] → C-4 [CURRENT]
```

**WHY lazy updates matter:**
Instead of updating A-6 and E-7 every time C-4 changes, we wait until someone actually needs them. This prevents doing 30 updates when C-4 changes 6 times in a day.

### Step 4: Work Continuation

**Agent reads work history index:**
```
Path: 2--(A-1)_(Sub_Bnch)_(O-F)/(A-1)_(Work)_(History)_(Index).md
```

**Determines where to continue:**
• Last work history entry
• Outstanding tasks from O-F
• Dependencies that are now unblocked


------------------------------------------------------

## Update Procedures

### Updating Sub-Branch O-F (NEW TASK-BASED STRUCTURE)

**Every work session updates the task tracking system:**

```markdown
# (A-1)_(Sub_Bnch)_(O-F).md

## DELIVERABLE DEFINITION
[One clear sentence defining what this sub-branch produces]

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
[Same structure...]

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

**WHY This Structure:**
• Tasks = Long-term memory (what's been done)
• Progress indicators = Current position
• Summaries = Quick context without reading work files
• Insights = Attached to relevant work
• Dependencies = Clear tracking with Git commit hash

### Updating Main Branch O-F

**Main branch SHORT-TERM MEMORY:**
```markdown
Entry 3: A-1 active - Working on base agents
Entry 2: A-2 complete - Error handling done
Entry 1: A-3 planned - Routing system next
```

**Git commit for tracking updates:**
```bash
# Commit your O-F changes with proper message
git add "*O-F*.md"
git commit -m "$(date '+%Y-%m-%d'): A-1: Updated O-F"

# Now the timestamp is tracked in Git history
```

**NOTE:** Master Timestamp Log DEPRECATED (Decision: 2025-09-04)
All timestamps tracked via Git commit history.

### Updating Trunk O-F

**CONDITIONS for trunk update:**
1. Tech spec change (needs verification)
2. Project-wide insight discovered
3. Branch status change (complete/blocked/active)
4. New dependency identified

**Trunk SHORT-TERM MEMORY update:**
```markdown
Entry 3: Branch A-1 active - Base agents in progress
[Only pointers, no details]
```

**Trunk LONG-TERM MEMORY update:**
```markdown
## Branch A (Agent System)
- Status: Active
- Progress: A-1 (80%), A-2 (complete)
- Dependencies: Blocks C
- Notes: Consider different LLM providers
```

**Trunk INSIGHTS update (only if project-wide):**
```markdown
💡 **Docker networking breaks with VPN**
- Containers can't reach each other when VPN active
- Solution: Disconnect VPN or use host networking
```


------------------------------------------------------

## Branch Creation Protocol

### Step 1: Determine If New Branch Needed

**Main Branch Creation Triggers:**
• New major system component or domain (Agents, API, Database)
• Logical grouping of related functionality
• Organizational clarity

**Sub-Branch Creation Triggers:**
• New deliverable within the domain
• One clear objective that can be completed
• Produces something testable/verifiable

**CRITICAL DECISION (2025-09-01):** 
Branches based on DELIVERABLES, not tokens!
- Main branch = Major system component
- Sub-branch = Specific deliverable
- Continue in same sub-branch if work relates to deliverable
- New sub-branch ONLY for genuinely new deliverable

### Step 2: Propose Sub-Branch in Propositions Sheet

**Location:** `[Main_Branch]/0.2--(Sub-Bnch)_(Propositions)/(Sub-Bnch)_(Propositions).md`

**What This Is:**
A document where agents write proposals for new sub-branches they think are needed. This prevents agents from creating random sub-branches and gives Chris visibility into what's being considered.

**Format for propositions (4-5 sentences explaining the deliverable):**
```markdown
### [Proposed Sub-Branch Name]: [Brief Description]  
**Proposed by:** [Agent identifier] on [Date/Time]
**Why needed:** [4-5 sentences explaining: What specific deliverable this will create. Why it's a separate deliverable from existing sub-branches. What problem it solves or capability it adds. How it fits within the main branch's domain. Any dependencies or relationships to other sub-branches.]
**Notes:** [Optional additional context that might help Chris decide]
```

**Example Format (not real branch):**
```markdown
### X-4: Error Recovery System
**Proposed by:** Agent working on X-3 on 2025-09-01 | 14:30 EST
**Why needed:** This sub-branch would create a complete error recovery system as a distinct deliverable. While X-2 handles basic error catching, recovery involves retry logic, fallback strategies, and state restoration which is a separate concern. This deliverable would produce a tested recovery module that other branches could use. It needs to be separate from X-2 because recovery strategies are independent of error detection.
**Notes:** Discovered need while working on X-3 when transient failures kept breaking the workflow.
```

**WHY propositions matter:**
Agents capture ideas without getting distracted. Chris reviews during planning. Nothing gets lost.

**NOTE:** Branch creation authority = Agents propose, Chris decides (Decision: 2025-09-01)

### Step 3: Complete Context Analysis Protocol

**CRITICAL:** This protocol runs BEFORE any coding begins and whenever new needs are discovered.

## Task Analysis Protocol (BEFORE Starting Work)

### When This Triggers
**MANDATORY:** Before starting ANY sub-task implementation
**CRITICAL:** This prevents 95% of mid-task discoveries if done THOROUGHLY

### The Analysis Process (EXHAUSTIVE - Not Half-Assed)

```markdown
TASK: [What I'm about to implement]

## 1. FORCED DECOMPOSITION (Chris's Requirement)
- Break into MICRO-STEPS (not vague components):
  * Step 1: [Exact action, e.g., "Create error class"]
  * Step 2: [Exact action, e.g., "Add retry decorator"]
  * Step 3: [Each step should be 5-10 lines of code max]
- Patterns required:
  * [Specific pattern with implementation details]
- Data flow:
  * Input: [What comes in]
  * Processing: [What happens]
  * Output: [What goes out]

## 2. INTEGRATION POINT ANALYSIS (Critical)
- Where this touches other code:
  * [Branch X, line Y]: Will call this method
  * [Branch Z]: Needs this error type
  * [Branch W]: Shares this pattern
- Potential conflicts:
  * [What could break]
  * [What might be incompatible]

## 3. CONTEXT INVENTORY (What I Actually Have)
From my O-F:
- [Specific component, not "stuff from O-F"]

From my dependencies:
- [Exact import with version/timestamp]

From work history:
- [Specific implementation, file, line number]

## 4. GAP IDENTIFICATION (Be Paranoid)
Missing (check thoroughly!):
- [Component X doesn't exist - searched where?]
- [Pattern Y undefined - checked which branches?]
- [Decision Z needed - about what specifically?]

## 5. ASSUMPTION DOCUMENTATION (No Hidden Assumptions)
I'm assuming:
- [List EVERY assumption, even "obvious" ones]
- [E.g., "Auth tokens are strings"]
- [E.g., "Errors can be serialized to JSON"]
- [E.g., "Retry count is less than 10"]

Verified facts:
- [What I've actually confirmed]
- [Where I confirmed it]

## 6. RESOLUTION PLAN (Complete Before Coding)
- Import from [Branch] for [specific need]
- Build [component] locally because [reason]
- Research [unknown] before starting
- FLAG FOR CHRIS: [Specific decision needed]
```

**Why This THOROUGH Analysis Matters:**
Chris's insight: "If the code you're writing has to do with your plan already, then shouldn't you already know what those gaps are?"

The solution isn't mid-task checkpoints. It's making the upfront analysis ACTUALLY EXHAUSTIVE.

**Signs of Half-Assed Analysis (DON'T DO THIS):**
• "I need error handling from A-2" (Too vague!)
• "Import auth stuff from B-3" (What specifically?)
• "Use retry pattern" (Which one? How?)

**Signs of PROPER Analysis:**
• "Need BaseError class from A-2, lines 45-67, for inheritance"
• "Import OAuth2 refresh method from B-3, not the full auth system"
• "Use exponential backoff with 2^n seconds, max 3 retries, from B-3's pattern"

## THE CONTEXT ANALYSIS GATES SYSTEM

### When This Protocol Triggers

**Trigger Point 1: New Sub-Branch Creation**
```
Agent proposes A-3 → Chris approves → Create structure
→ MUST RUN CONTEXT ANALYSIS before any work
```

**Trigger Point 2: Task Analysis Reveals Needs (MECHANICAL TRIGGER)**
```
Run THOROUGH Task Analysis Protocol (see above)
→ Analysis reveals: "Need retry logic but don't have it"
→ RUN CONTEXT ANALYSIS GATES to find it
→ Import it if found, build it if not
```

**Note:** LLMs DON'T spontaneously realize needs - the Task Analysis Protocol FORCES discovery

**Trigger Point 3: Hitting a Blocker**
```
Can't proceed: "Need auth strategy but it doesn't exist"
→ RUN PREREQUISITE PROCEDURE (Gate 0)
→ Cannot continue until resolved
```

### The Gates System - Complete Details

#### GATE 0: Prerequisites Check
**What doesn't exist yet but I NEED to start?**

```markdown
Before you can even begin, list what's required:
• "Need API specs defined" → Do they exist? Check indexes
• "Need database schema" → Created yet? Scan branches
• "Need auth strategy" → Documented? Search propositions

If missing prerequisite found:
→ STOP - Cannot proceed
→ Document what's missing and why needed
→ Either:
   1. Research and document it (no assumptions!)
   2. Propose new sub-branch to build it
   3. Ask Chris for the missing information

NEVER ASSUME OR GUESS - Get real answers
```

**Prerequisite Resolution Process:**
```markdown
When Gate 0 triggers:

1. Document in handoff file:
   ## BLOCKED - Missing Prerequisites
   - Need: Database schema for users
   - Why: Can't build user API without data structure
   - Searched: C branch (not found)
   - Proposed: C-5 for schema design

2. Check propositions sheet:
   Path: [Main_Branch]/0.2--(Sub-Bnch)_(Propositions)/
   - Maybe someone already proposed it?
   - Status: PROPOSED/APPROVED/REJECTED?

3. If not proposed, add proposition:
   ### C-5: Database Schema Design
   **Proposed by:** [Agent] on [Date/Time]
   **Why needed:** B-2 needs schema before building endpoints.
   This deliverable would define all tables, relationships,
   and constraints for the user management system.
   **Status:** PROPOSED [Awaiting Chris]

4. If research needed instead:
   - Document research requirements
   - Do the research (check docs, standards, etc.)
   - Document findings in work history
   - NO ASSUMPTIONS - only documented facts
```

#### GATE 1: Necessity Check
**What do I NEED to complete my deliverable?**

```markdown
Scan indexes to find what exists:

1. Check Main Branch Index:
   Path: 0.1--(Index)_(Main_Bnchs)/
   Quick scan: A=Agents, B=API, C=Database

2. Check relevant Sub-Branch Indexes:
   Path: [Branch]/0.1--(Index)_(Sub-Bnchs)/
   See deliverables: A-1 (base), A-2 (errors)

3. For promising branches, check Work History Index:
   Path: [Sub-Branch]/(X-N)_(Work)_(History)_(Index).md
   5-7 word summaries show what's built

List your NEEDS:
• "Must have base class to extend"
• "Must have auth logic for API calls"
• "Must have user models"

If branch has something you NEED → RELEVANT
Cannot complete without it → RELEVANT
```

#### GATE 2: Optimization Check  
**What would make my deliverable BETTER?**

```markdown
While scanning, note optimizations:
• "Logging would help debugging"
• "Caching would improve performance"
• "Retry logic would add resilience"

These aren't required but would improve quality.

If branch offers optimization → RELEVANT (mark as optional)
Document why it would help
```

#### GATE 3: Duplication Check
**Does this already exist somewhere?**

```markdown
Before building ANYTHING:
1. Quick scan of all indexes
2. Check if another branch built it
3. Even partial implementations count

If it exists → RELEVANT (import it)
Why build something twice? That's stupid.

Examples:
• About to build retry logic? B-3 has it!
• Creating error types? A-2 defined them!
• Need logging? D already built it!
```

#### GATE 4: Uncertainty Check
**Not sure if something would help?**

```markdown
Can't decide if Branch X's feature Y is useful?

→ FLAG FOR CHRIS:
"Chris, I'm building [deliverable].
Branch X has [feature Y].
Should I import it for [purpose]?"

Chris decides, not you.
This prevents bad architecture decisions.
```

### The Extraction Rules

**CORE PRINCIPLE:**
> "Extract ONLY what you cited as the reason for relevance."

```markdown
## How to Extract:

1. Look at WHY you marked it RELEVANT:
   - Said "need auth flow" → Take ONLY auth flow
   - Said "need base class" → Take ONLY class structure
   - Said "need models" → Take ONLY model definitions

2. Leave behind:
   - Implementation details specific to that branch
   - Their domain-specific logic
   - Their test data
   - Their error messages
   - Anything NOT cited as needed

3. Document what you took:
   ## Shared Context Sources:
   - B-3: Auth flow sequence [2025-09-01 | 14:00 EST]
     * Took: OAuth2 flow steps
     * Left: Actual implementation
     * Why: Need the pattern, not the code
```

### Warning Signs (Smell Test)

```markdown
## 🚨 Over-importing Warning:
- Importing from >4 branches
- Context files getting huge
- Taking entire files instead of pieces
→ Review with Chris

## 🚨 Under-importing Warning:
- Zero imports (unless truly standalone)
- Rebuilding existing solutions
- Spending hours on solved problems
→ Re-run duplication check
```

### Complete Example: Creating A-3 (Error Recovery)

```markdown
## RUNNING CONTEXT ANALYSIS FOR A-3

### GATE 0 - Prerequisites:
Need: Error scenarios documented
Check: Scanning indexes... NOT FOUND
Action: Research common agent failures
[Research completed, documented in work history]
✓ Gate 0 passed

### GATE 1 - Necessity:
Scanning for NEEDS:
• Base agent structure → A-1 has it ✓ RELEVANT
• Error types defined → A-2 has them ✓ RELEVANT
• Must-have items found

### GATE 2 - Optimization:
Scanning for improvements:
• Logging for errors → D has patterns ✓ RELEVANT (optional)
• Retry for transient failures → B-3 has logic ✓ RELEVANT (optional)

### GATE 3 - Duplication:
About to build:
• Error recovery system → Checking... doesn't exist ✓
• Retry mechanism → Wait, B-3 has this! Import it

### GATE 4 - Uncertainty:
• C-4 has caching... should failures be cached?
→ ASKING CHRIS: "Should error recovery cache failed requests?"

### EXTRACTION PLAN:
FROM A-1:
- TAKE: Base class structure only
- LEAVE: Agent-specific methods
- REASON: Need skeleton to add recovery to

FROM A-2:
- TAKE: Error type definitions
- LEAVE: Error handling implementation
- REASON: Need types, not their handling

FROM B-3:
- TAKE: Retry logic pattern
- LEAVE: API-specific implementation
- REASON: Need approach, not specifics

FROM D (optional):
- TAKE: Logging interface
- LEAVE: Log formatting details
- REASON: Want consistent logging

### DOCUMENTING IN A-3 O-F:
## Shared Context Sources:

### Required Imports:
- A-1: Base agent class [2025-09-01 | 12:00 EST]
  * Extracted: Class structure only
- A-2: Error types [2025-09-01 | 11:00 EST]
  * Extracted: Type definitions

### Optional Imports:
- B-3: Retry patterns [2025-09-01 | 14:00 EST]
  * Extracted: Retry logic approach
- D: Logging [2025-09-01 | 09:00 EST]
  * Extracted: Logging interface

### Pending Chris Decision:
- C-4 caching for failed requests?

## Dependency Chain:
Direct dependencies: A-1, A-2, B-3, D
A-1 depends on: [none]
A-2 depends on: A-1
B-3 depends on: B-1
D depends on: [none]
Full chain: A-3 → [A-1, A-2 → A-1, B-3 → B-1, D]
```

### Managing Dependencies

**IMPORTANT:** Mutual dependencies ARE allowed (Chris's clarification)
```markdown
A can need B while B needs A - this is fine!
System handles through:
• Proper abstraction layers
• Shared component branches
• Clear bidirectional documentation

Not about preventing circles, but managing them.
```

### Step 4: Create Branch Structure (After Chris Approves)

```bash
# For new main branch B:
# cd = "change directory" (move to a folder)
mkdir -p "0.2--(Trunk)_(Branch)_(System)/3--(B)_(Main_Bnch)_(O-F)/0--(README_Folder)"
mkdir -p "0.2--(Trunk)_(Branch)_(System)/3--(B)_(Main_Bnch)_(O-F)/0.1--(Index)_(Sub-Bnchs)"
mkdir -p "0.2--(Trunk)_(Branch)_(System)/3--(B)_(Main_Bnch)_(O-F)/0.2--(Sub-Bnch)_(Propositions)"
mkdir -p "0.2--(Trunk)_(Branch)_(System)/3--(B)_(Main_Bnch)_(O-F)/1--(B)_(Main_Bnch)_(O-F)"
# NOTE: No timestamp log folder - using master timestamp log instead

# For new sub-branch B-1:
mkdir -p "0.2--(Trunk)_(Branch)_(System)/3--(B)_(Main_Bnch)_(O-F)/2--(B-1)_(Sub_Bnch)_(O-F)"

# Expected output: Folders created with no error messages
```


------------------------------------------------------

## Update Cascade Examples (Step-by-Step)

### Example: Update Flowing Up (Branch → Trunk)

**Situation:** A-1 discovers Docker breaks with VPN active

```
Step 1: A-1 agent discovers issue
- Docker containers can't communicate when VPN active
- This affects B-2 which also uses Docker

Step 2: Update A-1's O-F
## Insights:
💡 **Docker breaks with VPN**
- Containers lose inter-communication
- Solution: Disconnect VPN or use host networking

Step 3: Evaluate scope
- Affects multiple branches? YES (B-2 uses Docker)
- Infrastructure issue? YES
- Project-wide impact? YES

Step 4: Promote to trunk
Update (Trunk)_(O-F).md:
## Session Insights:
💡 **Docker networking breaks with VPN**
- Affects all Docker-using branches
- Solution: Disconnect VPN during development

Step 5: Git commit prompt
"🟢 GIT COMMIT: Added Docker-VPN conflict to trunk insights"
```

### Example: Update Flowing Down (Trunk → Branch)

**Situation:** Trunk tech specs change Python version

```
Step 1: Trunk updated
- Python changed from 3.11 to 3.13
- New in Technical Setup section

Step 2: A-1 agent logs in next day
- Reads trunk O-F
- Compares with A-1's O-F tech specs
- Mismatch detected!

Step 3: Update A-1's tech specs
- Copy new Python version to A-1 O-F
- Check if affects A-1's work
- Update dependencies if needed

Step 4: Document update
In A-1 work history:
"Synchronized with trunk: Python 3.11 → 3.13"

Step 5: Git commit prompt
"🟢 GIT COMMIT: A-1 synchronized with trunk Python update"
```


------------------------------------------------------

## Common Scenarios (Complete Walkthroughs)

### Scenario 1: Creating New Sub-Branch

**Situation:** Need to create A-2 for error handling

**Steps:**
```
1. Agent working on A-1 identifies need for new deliverable
   - Error handling is separate deliverable from base classes
   - Will produce testable error management system
   
2. Add to propositions sheet:
   Path: 2--(A)_(Main_Bnch)_(O-F)/0.2--(Sub-Bnch)_(Propositions)/
   - Write 4-5 sentence explanation with timestamp
   - Include why it's needed and what it delivers
   
3. Chris reviews and approves during planning
   
4. Create structure:
   mkdir -p "0.2--(Trunk)_(Branch)_(System)/2--(A)_(Main_Bnch)_(O-F)/3--(A-2)_(Sub_Bnch)_(O-F)"
   
5. Create A-2 O-F with:
   - Objective: Add error handling to agents (deliverable)
   - Shared context: A-1 classes, D patterns
   - Dependency chain documented
   - Initial status: Planning
   
6. Update A's main O-F:
   - Add A-2 to sub-branch index
   - Update short-term memory
   
7. Update master timestamp log:
   - Add A-2 with initial timestamp
   
8. Git commit prompt:
   "🟢 GIT COMMIT: Created A-2 sub-branch for error handling"
```

### Scenario 2: Branch Needs External Context

**Situation:** A-1 needs B-3's authentication logic

**Steps:**
```
1. During A-1 work, realize need for auth

2. Check Master Timestamp Log for B-3's last update:
   Path: 0.2--(Trunk)_(Branch)_(System)/0.2--(Master)_(Timestamp)_(Log)/
   - B-3: 2025-09-01 | 14:00 EST
   
3. Read B-3's O-F for relevant sections
   
4. In A-1's O-F, add to dependency chain:
   ## Dependency Chain:
   Direct dependencies: B-3
   B-3 depends on: [check B-3's O-F]
   
   ## Shared Context Sources:
   - B-3: Auth logic [Timestamp: 2025-09-01 | 14:00 EST]
   
5. Extract needed parts from B-3

6. Continue work with context

7. On next login, check master log:
   - If B-3 updated after 14:00 EST, review changes
   - Update A-1 if needed
   
8. Git commit after adding dependency:
   "🟢 GIT COMMIT: A-1 added B-3 auth dependency"
```

### Scenario 3: Two Branches Merge

**Situation:** C and F merge into C-F

**Steps:**
```
1. Complete individual objectives of C and F
2. Identify overlap/integration needs
3. Create new C-F main branch:
   mkdir -p ".../5--(C-F)_(Main_Bnch)_(O-F)"
   
4. In C-F O-F:
   ## Origin:
   - Merged from C (cache) and F (frontend)
   - Original branches remain for reference
   
5. Parse relevant work from C and F:
   - Take final implementations
   - Combine insights
   - Merge dependencies
   
6. Update trunk:
   - Long-term memory shows C-F exists
   - Note C and F can still be developed independently
   
7. Original C and F remain intact for:
   - Historical reference
   - Independent future development
   - Rollback if needed
```


------------------------------------------------------

## Update Cascading Rules

### What Updates Flow Up (Branch → Trunk)

**Always flows up:**
• Tech specification changes
• Project-blocking issues
• Completed milestones
• New dependencies discovered

**Requires verification before flowing up:**
• Architecture changes
• Database schema modifications
• API contract changes
• Security-related updates

**Stays in branch:**
• Implementation details
• Local optimizations
• Branch-specific workarounds
• Work progress details

### What Updates Flow Down (Trunk → Branch)

**Always flows down:**
• Tech spec changes
• Project description updates
• New project-wide insights
• Dependency changes

**Checked on login:**
• All trunk changes since last session
• Related branch updates (if using shared context)
• Timestamp logs for context sources


------------------------------------------------------

## Git Integration Procedures

### Git Strategy - FINALIZED DECISION

**Architecture Decision:** Single Git branch (master/main)
• All documentation branches exist as folders
• NO separate Git branches for documentation
• Simple, visible, no branch switching

### Two-Commit Workflow (REQUIRED)

**The Problem:** 
When committing everything together, diffs show work history changes mixed with O-F updates, creating noise.

**The Solution:**
Two separate commits per work session:

```bash
# COMMIT 1: Work files
git add "[work_history_folder]/*" "[implementation_files]"
git commit -m "$(date '+%Y-%m-%d'): A-1: Implementation work"

# Update your O-F file with progress

# COMMIT 2: O-F file only  
git add "*O-F*.md"
git commit -m "$(date '+%Y-%m-%d'): A-1: Updated O-F"
git push origin master
```

### Dependency Checking via Git

**Old Way (Master Timestamp Log):**
• Check central log file
• See when each branch updated
• 20 dependencies = reading massive file

**New Way (Git-powered):**
```bash
# See all O-F updates across project
git log --grep="O-F" --oneline --since="2025-09-01"

# Check specific dependency changes
git diff [last-sync-commit] HEAD -- "path/to/dependency/O-F.md"
```

**Each O-F stores:**
```markdown
Last sync commit: abc123def
```

**Benefits at Scale:**
• 5 dependencies: Check via Git = 100 tokens vs 3,000 tokens
• 20 dependencies: Check via Git = 200 tokens vs 15,000 tokens!

### When to Prompt for Git Commit (EVERY UPDATE!)

**Chris's Rule:** "Every update (not only the ones that change the otherwise permanent areas) should have the agent prompt me to do a git commit"

**ALWAYS prompt after:**
• ANY update to trunk O-F
• ANY update to branch O-F  
• ANY update to sub-branch O-F
• ANY work history entry
• ANY README update
• Before switching branches
• Before ending session

**WHY prompt for everything?**
Chris said "I don't know much about Git" - frequent commits ensure nothing is lost and provide rollback points if something breaks.

**Prompt message format:**
```
🟢 GIT COMMIT NEEDED

Changes made:
- [Specific file/update 1]
- [Specific file/update 2]

Suggested commit:
git add -A && git commit -m "[Branch]: [Action] [Component]"

Run this? (or modify message)
```

**Example prompt:**
```
🟢 GIT COMMIT NEEDED

Changes made:
- Updated A-1 sub-branch O-F with progress
- Added work history entry for implementation
- Updated timestamp log in branch A

Suggested commit:
git add -A && git commit -m "A-1: Implement base agent class"

Run this? (or modify message)
```

### Commit Message Conventions

**Format:**
```
[BRANCH]: [Action] [Component]

Body:
- Specific change 1
- Specific change 2

Affects: [Dependencies]
```

**Example:**
```
A-1: Add base agent class with OpenAI

- Created agent.py with base class
- Added OpenAI integration
- Includes error handling

Affects: A-2 will build on this
```

**🔔 PENCILED: Full git strategy TBD**


------------------------------------------------------

## Work History Management

### Creating Work History Entries

**When to create new work history file:**
• Starting new phase of work
• Major milestone reached
• Switching focus within sub-branch
• After significant debugging session

**Work history naming (EXAMPLES - use descriptive names):**
```
1--(A-1)_(Setup)_(Initial)/
2--(A-1)_(Implementation)_(Core)/
3--(A-1)_(Testing)_(Debug)/
4--(A-1)_(Documentation)_(Final)/
```

**IMPORTANT:** These are example names - use whatever describes the actual work

### Updating Work History Index

**After each work history addition:**
```markdown
# In (A-1)_(Work)_(History)_(Index).md

## Work History:
1. **Setup Initial** - Environment and dependencies configured
2. **Implementation Core** - Built base agent class with methods
3. **Testing Debug** - Fixed connection issues and error handling
4. **Documentation Final** - Added docstrings and usage examples
```

**Index should be scannable:**
• 5-7 word descriptions
• Clear progression visible
• Easy to find specific work


------------------------------------------------------

## Agent Handoff Procedures

### When Switching Agents

**Exiting agent must:**
1. Complete all documentation updates
2. Update the handoff file
3. Run validator script
4. Prompt for git commit
5. Output summary with handoff file location

### Handoff File Management

**Location:** `(A-1)_(Handoff)_(Status).md` in each sub-branch folder

**Template for Handoff File:**
```markdown
# HANDOFF STATUS - Branch A-1
[Last Updated: 2025-09-01 | 22:30 EST | By: Claude-4.1-Opus]

## CURRENT STATUS
**Phase:** Implementation complete, testing started
**Completion:** ~75% of deliverable

## WORK COMPLETED THIS SESSION
• Created base agent class structure
• Implemented OpenAI integration
• Added error handling framework
• Started unit test suite

## NEXT STEPS
1. Finish remaining unit tests
2. Add retry logic for API calls
3. Implement logging system
4. Test with real API keys

## ACTIVE BLOCKERS
• **Missing API Keys:** Need real OpenAI/Anthropic keys in .env
• **Awaiting Decision:** Chris to confirm retry limit (3 or 5?)
• **Dependency Update:** B-3 auth module needs completion first

## DEPENDENCIES
• Imports from B-3: Authentication [Last checked: 14:00 EST]
• Imports from C-1: Database models [Current as of: 10:00 EST]

## NOTES FOR NEXT AGENT
• Watch for rate limiting on OpenAI calls
• The async handler is tricky - see comments in code
• Chris prefers 3 retries based on Discord discussion
```

**Update Frequency:** 
• At end of EVERY work session
• When hitting a major blocker
• Before any agent switch

### New Agent Onboarding

**New agent receives:**
1. Standard base documents
2. Trunk O-F
3. Specific branch O-F files
4. **Handoff file from sub-branch** (CRITICAL)
5. Work history for context

**First action:** Read handoff file to understand current state


------------------------------------------------------

## Error Recovery Procedures

### If Updates Conflict

**Scenario:** Two agents updated trunk simultaneously

**Recovery:**
1. Check git history for conflicts
2. Identify which updates are valid
3. Merge non-conflicting changes
4. Re-run synchronization
5. Document issue in LLM Limitations

### If Context Sharing Breaks

**Scenario:** A-1 has outdated B-3 context

**Recovery:**
1. Check B's timestamp log
2. Read current B-3 O-F
3. Identify what changed
4. Update A-1's context references
5. Review A-1 work for impacts
6. Document any required changes


------------------------------------------------------

## 🔔 PENCILED ITEMS - Operations Decisions

### Synchronization Frequency
**What needs deciding:** How often should agents check for updates?
**Options:** Every login, hourly, after major operations
**Consideration:** Balance between currency and efficiency

### Conflict Resolution Protocol
**What needs deciding:** Exact steps when updates conflict
**Context:** Rare but critical when it happens
**Current thought:** Manual review with Chris

### Validation Requirements
**What needs deciding:** What validations before trunk updates?
**Options:** Automated checks, manual approval, hybrid
**Consideration:** Speed vs safety

### Agent Assignment Method
**What needs deciding:** How agents know which branch to work on
**Context:** Need clear assignment mechanism
**Current thought:** Explicit in initial prompt


------------------------------------------------------

## Why This Document Matters

This operations manual ensures every agent follows the same procedures. Without consistent operations, the trunk-branch system becomes chaos. These workflows maintain order across parallel development.

Next document covers advanced systems and future considerations.


======================================================================
======================================================================
