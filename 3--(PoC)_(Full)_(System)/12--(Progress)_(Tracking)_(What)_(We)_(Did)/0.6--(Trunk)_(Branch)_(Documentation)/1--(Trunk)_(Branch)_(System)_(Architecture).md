# TRUNK-BRANCH DOCUMENTATION SYSTEM - ARCHITECTURE & PHILOSOPHY
## The Foundation for Parallel Project Development

[Created: 2025-09-01 | 03:45 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 04:20 EST | By: Claude-4.1-Opus]
[Revised: 2025-09-01 | 08:45 EST | By: Claude-4.1-Opus | Major updates: dependency chains, deliverable-based branches]
[Revised: 2025-09-01 | 20:30 EST | By: Claude-4.1-Opus | Fixed: removed token refs, clarified system design]
[Revised: 2025-09-03 | 10:15 EST | By: Claude-4.1-Opus | Added: Context Analysis Guidelines philosophy]
[Document 1 of 4 in Trunk-Branch System Documentation]


------------------------------------------------------

## What The Fuck Is This?

This is a complete redesign of our documentation system to enable multiple agents to work on different parts of the Fractal-RMO project simultaneously without stepping on each other.

• **Current Problem:** Single documentation stream = agents overwrite each other
• **Solution:** Trunk (shared core) + Branches (isolated work areas)
• **Result:** Parallel development with coordinated updates


------------------------------------------------------

## Why This System Exists

### The Problem We're Solving:

**Single-threaded documentation creates bottlenecks:**
• Agent A works on API endpoints
• Agent B works on database setup
• Both update the same Project Overview file
• 💥 Conflicts, overwrites, lost work

**Context pollution:**
• Every agent sees every detail of every other part
• Irrelevant information clutters their context window
• Important branch-specific insights get lost in the noise


------------------------------------------------------

## Core Concepts

### The Trunk

**What it is:**
• The source of truth for the entire project
• Contains only project-wide essentials
• Every agent reads from here
• Highly protected from random changes

**What goes in the trunk:**
• Project description & mechanics (what Fractal-RMO is)
• Technical setup (shared dependencies, ports, configs)
• LLM Limitations document (project-wide failure patterns)
• Project-wide insights (gotchas that affect multiple areas)
• Long-term memory of all branches (overview of what exists)
• Short-term memory pointers (what's actively being worked on)

**What DOESN'T go in the trunk:**
• Detailed work progress (that's in branches)
• Branch-specific insights (unless they affect other branches)
• Implementation details (stay in relevant branches)

**WHY the trunk exists:**
The trunk prevents every agent from seeing every detail of every other branch's work. Without it, an agent working on database connections would have to wade through API endpoint details, agent error handling specifics, and dozens of other irrelevant items. The trunk gives everyone the bird's eye view while keeping details isolated.


------------------------------------------------------

### Branches

**What they are:**
• Isolated work areas for specific project components
• Have their own documentation systems
• Can be organizational (main branches) or deliverable-based (sub-branches)
• Each sub-branch includes a handoff file for session continuity

**Main Branches (Organizational):**
• Created for major system components/domains (e.g., "Agent System", "API Development")
• Represent logical groupings of related functionality
• Can contain multiple sub-branches
• Example: `2--(A)_(Main_Bnch)_(O-F)` for agent development

**Sub-Branches (Deliverable-Based):**
• Created for specific deliverables within a domain
• One clear objective that can be completed
• Produces something testable/verifiable
• Actual work happens here
• Example: `2--(A-1)_(Sub_Bnch)_(O-F)` for base agent creation

**Branch Scope Determination:**
```
NOTE: Branch scope determined by deliverables, not tokens
(Decision: 2025-09-01)

Main Branch = Major system component
Examples:
- A = Agent System (all agent-related work)
- B = API Development (all endpoints)
- C = Database Layer (all DB work)

Sub-Branch = Specific deliverable within domain
Examples under Agent System (A):
- A-1 = Base agent classes (deliverable: working base class)
- A-2 = OpenAI integration (deliverable: OpenAI agent functional)
- A-3 = Error handling (deliverable: agents handle errors gracefully)

Work continues in same sub-branch if related to deliverable
New sub-branch only for genuinely new deliverable
```


------------------------------------------------------

## Overview Files (O-F)

### What Are O-F Files?

**Definition:**
• Evolved from our current `0.2--(Project)_(Overview)_(Current)_(State)`
• Each level (trunk, branch, sub-branch) has its own
• Contains memory systems, insights, and status

**Naming Convention:**
• Trunk: `(Trunk)_(O-F)`
• Main Branch: `(A)_(Main_Bnch)_(O-F)` 
• Sub-Branch: `(A-1)_(Sub_Bnch)_(O-F)`

**Key Principle:**
Every O-F file serves its specific scope - trunk serves project-wide needs, branches serve their domain


------------------------------------------------------

## Memory System Architecture

### Trunk Memory Systems

**SHORT-TERM MEMORY (CRITICAL - Just Pointers!):**
• Points to actively worked branches ONLY
• Contains ZERO work details - just branch names and one-line status
• NO implementation details, NO specific progress, NO technical details

**WHY just pointers?**
If the trunk contained actual work details, every single agent would have to read through database implementation details, API endpoint specifics, error handling code, and dozens of other irrelevant items just to get to their own work. The trunk would become a massive wall of text that pollutes every agent's context window.

**Example of CORRECT trunk short-term memory:**
```markdown
Entry 3: Branch A-1 active - Base agent work
Entry 2: Branch B-2 complete - API auth done
Entry 1: Branch C planning - Cache design phase
```

**Example of WRONG trunk short-term memory:**
```markdown
Entry 3: Branch A-1 created base_agent.py with OpenAI integration... [NO! Too detailed!]
```

**If you need details:**
Go to that specific branch's O-F file for the actual work information

**LONG-TERM MEMORY:**
• Overview of all branches (active and inactive)
• Dependencies between branches
• Strategic priorities
• Example:
  ```
  Branch A (Agent System):
    - Status: In Progress
    - Sub-branches: A-1 (base agents), A-2 (error handling)
    - Dependencies: Blocks C (orchestrator)
    - Future: Consider different LLM providers
  ```


------------------------------------------------------

### Branch Memory Systems

**Main Branch SHORT-TERM MEMORY:**
• Points to its active sub-branches
• Similar to trunk but scoped to the branch

**Sub-Branch SHORT-TERM MEMORY:**
• Contains actual work details
• The "real" memory of what's been done
• Current format we use, but isolated to sub-branch

**Sub-Branch HANDOFF FILE:**
• Located at `(A-1)_(Handoff)_(Status).md`
• Updated at end of every session
• Contains: current status, work completed, next steps, blockers, dependencies
• Critical for agent continuity between sessions

**Branch INSIGHTS:**
• Branch-specific gotchas and learnings
• Only promoted to trunk if affects other branches


------------------------------------------------------

## Insight Management Philosophy

### Trunk Insights

**What belongs in trunk insights:**
• Gotchas that affect multiple branches
• System-wide issues (like "Python 3.13 breaks packages")
• Cross-cutting concerns
• Infrastructure problems

**What DOESN'T belong:**
• Branch-specific workarounds
• Implementation details
• Normal progress notes


### Branch Insights

**Stay in branch:**
• Implementation-specific gotchas
• Local workarounds
• Domain-specific learnings

**Promoted to trunk when:**
• Affects other branches
• Changes project-wide understanding
• Creates new dependencies


------------------------------------------------------

## Dependency Chain System & Update Strategy

### The Update Cascade Problem

**Without smart updates:**
C-4 updates → Must update A-6, B-2, C-F, E-7 immediately → Each of those updates 6 times → 30 total updates!

**With dependency chains (Chris's solution):**
C-4 updates → Document it → Updates cascade ONLY when needed

### How Dependency Chains Work

**Each sub-branch O-F documents:**
```markdown
## Dependency Chain:
Direct dependencies: C-4, D-1
C-4 depends on: [none]
D-1 depends on: B-3
Full chain: A-6 → [C-4] + [D-1 → B-3]
```

**Master Timestamp Log tracks all updates:**
```markdown
# Master Timestamp Update Log
[Location: 0.2--(Trunk)_(Branch)_(System)/(Master)_(Timestamp)_(Log).md]

## Sub-Branch Updates:
- A-1: 2025-09-01 | 15:30 EST
- A-6: 2025-09-01 | 12:00 EST
- C-4: 2025-09-01 | 17:00 EST ← Updated after A-6!
```

### Lazy Update Strategy

**Chris's Example Scenario:**
```
E-7 depends on A-6
A-6 depends on C-4
C-4 gets updated

OLD WAY: Update A-6 immediately, then E-7
NEW WAY: Wait until someone needs A-6 or E-7
```

**When E-7 agent starts:**
1. Check dependency chain: E-7 → A-6 → C-4
2. Check Master Timestamp Log
3. See C-4 updated after A-6's last sync
4. Block E-7 with message:
```
🔴 STARTUP BLOCKED - Dependency Chain Issue

E-7 cannot proceed because:
• E-7 depends on A-6 (last synced: 12:00 EST)
• A-6 depends on C-4 (updated: 17:00 EST)
• A-6 needs update from C-4 first

To resolve:
1. Run update agent on A-6, or
2. Manually update A-6 with C-4's context
```

### Update Agent Role

**When multiple branches need updates:**
• Update agent takes the dependency list
• Efficiently updates all affected O-F files
• Doesn't need full context docs (saves tokens)
• Reports completion

**Key Principle:**
Updates happen just-in-time, not immediately. This prevents cascading update storms while maintaining consistency.


------------------------------------------------------

## Information Flow

### Upward Flow (Branch → Trunk)

**Automatic updates to trunk:**
• Tech spec changes (with verification)
• Project-wide insights
• Branch status for long-term memory

**Manual promotion decisions:**
• Whether an insight is project-wide
• Whether to merge branches
• Whether to change dependencies


### Downward Flow (Trunk → Branch)

**On agent login:**
• Sync tech specs from trunk
• Pull project-wide insights
• Check for dependency changes

**During work:**
• Regular checks of trunk for updates
• Verification before making trunk changes


------------------------------------------------------

## Why This Architecture Works

### For Chris's ADHD:

**Clear separation:**
• Trunk = bird's eye view
• Branches = focused work areas
• No mixing of concerns

**Visual organization:**
• Can see all active work at a glance
• Dependencies are explicit
• Progress is trackable


### For LLM Agents:

**Context efficiency:**
• Only see relevant information
• No pollution from other domains
• Clear scope boundaries

**Conflict prevention:**
• Isolated work areas
• Explicit merge procedures
• No accidental overwrites


### For Project Scaling:

**Unlimited parallel work:**
• As many branches as needed
• Each with its own documentation
• Coordinated through trunk

**Maintains coherence:**
• Trunk ensures consistency
• Synchronization catches issues
• Dependencies tracked explicitly


------------------------------------------------------

## System Principles

### Core Principles (Don't Change These):

1. **Trunk is source of truth** - All shared info lives here
2. **Branches are isolated** - Work happens in branches
3. **Explicit dependencies** - Nothing implicit or assumed
4. **Verification before trunk changes** - Protect shared state
5. **Context efficiency** - Agents only see what they need


### Implementation Details (Can Evolve):

• Exact folder structure
• Specific update procedures  
• Synchronization frequency
• Tool choices


------------------------------------------------------

## Branch Merging Philosophy

### Why Branches Remain After Merging

**The Scenario:**
Branches C (cache system) and F (frontend) need integration, so we create C-F.

**CRITICAL UNDERSTANDING:**
• C and F branches DON'T disappear
• C-F is a NEW branch that combines them
• Original C and F remain for independent development

**WHY keep originals?**
```
Example: After C-F merge
- C branch discovers a cache optimization specific to backend
- This optimization doesn't affect frontend (F)
- Developer works in C branch with full C context
- No F code cluttering the view
- Once tested, update flows to C-F if relevant
```

**Chris's exact reasoning:**
"What if the C branch needs more development, which is specific to the C branch yet not the F branch? It should be able to be changed with the full context of C, without F muddying it."

**Update flow after merge:**
```
C branch updated → Check if affects C-F → Update C-F if needed
F branch updated → Check if affects C-F → Update C-F if needed
C-F develops independently → Updates don't flow back to C or F
```


------------------------------------------------------

## Comparison With Current System

### Current System:
```
Single Project Overview → Everyone updates → Conflicts
Single work history → Everyone adds → Confusion  
Single insight list → Everything mixed → Noise
```

### Trunk-Branch System:
```
Trunk Overview → Points to branches → Coordination
Branch work history → Isolated progress → Clarity
Scoped insights → Relevant to domain → Efficiency
```


------------------------------------------------------

## Next Steps for Implementation

**Immediate Actions:**
1. Convert current O-F to Trunk O-F
2. Create first main branch structure
3. Update contribution guidelines for branch workflow
4. Test with single branch before scaling

**See Other Documents:**
• File 2: Complete directory structure and naming
• File 3: Operational procedures for agents
• File 4: Advanced systems (context sharing, sync)


------------------------------------------------------

## Common Misconceptions to Avoid

### Misconception 1: "Merged branches disappear"
**Reality:** C and F create C-F, but C and F remain for independent work

### Misconception 2: "Trunk has all the details"
**Reality:** Trunk has ONLY pointers and project-wide info

### Misconception 3: "Branches are isolated forever"
**Reality:** Branches can share context through documented imports

### Misconception 4: "One agent per branch"
**Reality:** Multiple agents can work on sub-branches within a main branch


------------------------------------------------------

## 🔔 MASTER LIST OF PENCILED ITEMS

### Branch Creation Triggers
**RESOLVED (2025-09-01):** Branches based on deliverables, not tokens
• Main branches: Major system components/domains
• Sub-branches: Specific deliverables within domain
• Continue in same sub-branch if work relates to deliverable
• New sub-branch only for genuinely new deliverable

### Verification Protocol
**What needs deciding:** Exact steps for trunk modification approval
**Why it matters:** Protects shared state from corruption
**Options:**
• Automatic with warnings
• Always require confirmation
• Smart detection of sensitive changes
**Current thought:** Agent prompts Chris for sensitive changes

### Context Analysis Guidelines
**RESOLVED (2025-09-03):** Complete guidelines developed
• Gates system for evaluating relevance
• Extraction rules based on cited needs
• Prerequisites handling for missing components
• See full details in Document 3 Operations Manual

### Git Integration Strategy
**RESOLVED (2025-09-04):** Single Git branch approach with two-commit system

**Architecture Decision:** 
• Use master/main branch only - all doc branches as folders
• NO separate Git branches for documentation
• Simpler than multiple Git branches, no branch switching needed
• All documentation visible at once

**The Two-Commit System (CRITICAL FOR CLEAN DIFFS):**

**Why Two Commits?**
When committing everything together, diffs show work history changes mixed with O-F updates, creating noise that makes it hard to see what actually changed in the documentation structure.

**Implementation:**
```bash
# COMMIT 1: Work files (actual work done)
git add "[work_history_folder]/*" "[implementation_files]"
git commit -m "$(date '+%Y-%m-%d'): A-1: Implementation work"

# Now update your O-F file with task progress

# COMMIT 2: O-F files only (documentation structure)
git add "*O-F*.md"
git commit -m "$(date '+%Y-%m-%d'): A-1: Updated O-F"

# Push both commits
git push origin master
```

**Dependency Checking via Git:**
```bash
# See all O-F updates across project
git log --grep="O-F" --oneline --since="last-sync"

# Check if specific dependency changed
git diff [last-sync-commit] HEAD -- "path/to/dependency/O-F.md"
```

**Each O-F Stores Its Last Sync:**
```markdown
Last sync commit: abc123def
```

**Benefits at Scale:**
• 5 dependencies: Check via Git = 100 tokens vs 3,000 tokens reading files
• 20 dependencies: Check via Git = 200 tokens vs 15,000 tokens!
• Master Timestamp Log DEPRECATED - Git commit history replaces it entirely

**Commit Message Format:**
```
YYYY-MM-DD: [Branch-ID]: [Action] [Component]
Example: 2025-09-04: A-1: Updated task breakdown
```


------------------------------------------------------

## Context Analysis Philosophy

### Why Agents Need Structured Guidelines

**The Core Problem:**
Without clear rules, agents face two failure modes:
• **Over-importing:** Grabbing everything that might be useful, polluting their context with irrelevant code
• **Under-importing:** Missing existing solutions, rebuilding what's already been built

Both waste resources and create inconsistencies.

### The Balance Point

**The fundamental principle:**
> "If it exists and you need it, use it. Don't build it twice."

This simple rule drives everything, but applying it requires structured thinking:
1. **Know what you need** - Both required and optimal components
2. **Find what exists** - Efficient scanning via indexes
3. **Take only what's relevant** - Extract specific pieces, not entire implementations
4. **Handle what's missing** - No assumptions, get real answers

### Prerequisites: The Hidden Blocker

**A critical insight:**
Sometimes what you need doesn't exist yet. This isn't a failure - it's a discovery. When agents hit missing prerequisites:
• They must stop and document what's needed
• Either research to fill the gap
• Or propose new sub-branches to build it
• Never assume or guess

### The Extraction Principle

**Key rule:**
> "Extract ONLY what you cited as the reason for relevance."

If you said you need "auth flow", take the auth flow - not the entire auth system. This prevents context pollution while ensuring necessary reuse.

### Managing Dependencies

**Important clarification:**
Mutual dependencies CAN exist (A needs B, B needs A). The system handles this through:
• Proper abstraction layers
• Shared component branches
• Clear documentation of bidirectional needs

The goal isn't to prevent all circular references, but to manage them consciously.

### The Gates System

Agents evaluate branches through sequential gates:
• **Gate 0:** Prerequisites - What doesn't exist but I need?
• **Gate 1:** Necessity - What must I have?
• **Gate 2:** Optimization - What would make it better?
• **Gate 3:** Duplication - Does this already exist?
• **Gate 4:** Uncertainty - Should I ask Chris?

This creates a repeatable, mechanical process that removes guesswork.

### When Context Analysis Happens

**Three trigger points:**
1. **Sub-branch creation** - Before any work begins
2. **During work** - When discovering new needs
3. **Hitting blockers** - When prerequisites are missing

This ensures context is always evaluated, never assumed.


------------------------------------------------------

## Why This Document Matters

This architecture document is the foundation. Without understanding WHY we're doing trunk-branch, the HOW doesn't make sense. Every design decision flows from these principles.

Next document explains WHERE everything lives (complete structure).


======================================================================
======================================================================
