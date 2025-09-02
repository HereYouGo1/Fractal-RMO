# TRUNK-BRANCH DOCUMENTATION SYSTEM - OPERATIONS MANUAL
## Complete Agent Workflows and Update Procedures

[Created: 2025-09-01 | 03:48 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 04:30 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 09:30 EST | By: Claude-4.1-Opus | Major updates: master timestamp log, dependency chains, deliverable-based branches]
[Revised: 2025-09-01 | 20:40 EST | By: Claude-4.1-Opus | Fixed: clarified system design, proper documentation protocol]
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

**Agent reads Master Timestamp Log:**
```
Path: 0.2--(Trunk)_(Branch)_(System)/0.2--(Master)_(Timestamp)_(Log)/(Master)_(Timestamp)_(Log).md
```

**WHY this matters:**
The master timestamp log tells you when EVERY sub-branch last updated. Without checking this, you might work with outdated context and create inconsistencies.

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

### Updating Sub-Branch O-F

**Every work session updates:**
```markdown
## SHORT-TERM MEMORY
Entry 3: [New work today]
Entry 2: [Previous Entry 3]
Entry 1: [Previous Entry 2]
[Delete old Entry 1]

## CURRENT PHASE
[What just completed]

## NEXT PLANNED WORK
[Immediate next task]

## INSIGHTS (only if found gotcha)
💡 **[Specific trap/issue]**
- [One line problem]
- [One line solution]
```

### Updating Main Branch O-F

**Main branch SHORT-TERM MEMORY:**
```markdown
Entry 3: A-1 active - Working on base agents
Entry 2: A-2 complete - Error handling done
Entry 1: A-3 planned - Routing system next
```

**Master Timestamp Log update (NOT individual branch logs):**
```markdown
# In 0.2--(Trunk)_(Branch)_(System)/0.2--(Master)_(Timestamp)_(Log)/(Master)_(Timestamp)_(Log).md
- A-1: 2025-09-01 | 15:30 EST
- A-2: 2025-09-01 | 14:00 EST
[Update the timestamp for the sub-branch that just worked]
```

**NOTE:** Individual branch timestamp logs REMOVED (Decision: 2025-09-01)
All timestamps go in the master log for centralized tracking.

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

### Step 3: Detailed Context Requirement Protocol

**CRITICAL:** Chris specified this needs a structured analysis when creating any branch

**The Complete Protocol:**

```markdown
## DETAILED CONTEXT REQUIREMENT PROTOCOL
## For: Creating Sub-Branch [BRANCH-ID]

### STEP 1: Define Primary Objective
**What is this branch trying to accomplish?**
- Primary goal: [One clear sentence]
- Success criteria: [What defines completion]
- Token budget: [Estimated tokens needed]

### STEP 2: Scan ALL Existing Branches
**Review EVERY branch in the system:**

| Branch | Purpose | Relevance | Reason |
|--------|---------|-----------|--------|
| A-1 | Base agents | RELEVANT | Has class structure we need |
| A-2 | Error handling | RELEVANT | Need error patterns |
| A-3 | Routing | NOT RELEVANT | Different domain |
| B-1 | User auth | MAYBE | Similar patterns |
| B-2 | Data endpoints | NOT RELEVANT | Different focus |
| C-1 | Database | RELEVANT | Need connection logic |
| D | Logging | NOT RELEVANT | Will implement own |

### STEP 3: Evaluate What to Extract
**For each RELEVANT branch, specify extraction:**

FROM A-1:
- EXTRACT: Base class structure only
- IGNORE: Agent-specific logic
- REASON: Need foundation, not implementation

FROM A-2:
- EXTRACT: Error handling patterns
- IGNORE: Agent-specific errors
- REASON: Patterns applicable, specifics not

FROM C-1:
- EXTRACT: Connection pooling logic
- IGNORE: Query implementations
- REASON: Need connection management only

### STEP 4: Justify Context Imports
**Why does this branch need external context?**
- Without A-1 context: Would rebuild base class (waste)
- Without A-2 context: Would create inconsistent error handling
- Without C-1 context: Would duplicate connection logic

### STEP 5: Document in Branch O-F
**Add to new branch's O-F file:**

## Shared Context Sources
[Document all imports with timestamps]

### Full Context Imports:
- B-1: Complete endpoint structure [2025-09-01 | 10:00 EST]
  * Using as template for similar endpoints

### Partial Context Imports:
- A-1: Base class only [2025-09-01 | 09:30 EST]
  * Extracting foundation, not logic
- C-1: Connection pooling [2025-09-01 | 08:00 EST]
  * Using connection management pattern

### Context Dependencies:
- Critical: C-1 (breaks if connection pattern changes)
- Important: A-1 (inconsistent if base changes)
- Informational: B-1 (helpful but not required)
```

**WHY This Protocol Exists:**
Without structured analysis, branches either duplicate work (not checking what exists) or import too much (polluting their context). This protocol ensures efficient context reuse.

**🔔 PENCILED: Specific evaluation criteria**
• **What needs deciding:** Exact rules for RELEVANT vs NOT RELEVANT
• **Why it matters:** Prevents over/under importing
• **Chris's note:** "Guidelines have not yet been determined"

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
