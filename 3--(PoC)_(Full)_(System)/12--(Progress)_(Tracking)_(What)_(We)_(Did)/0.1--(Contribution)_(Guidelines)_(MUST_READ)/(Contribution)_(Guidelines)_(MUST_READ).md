# ⚠️ STRICT CONTRIBUTION PROTOCOL v2.0
## NUMBERED RULES WITH EXACT TEMPLATES - NO INTERPRETATION ALLOWED

[Protocol Version: 2.0 | Created: 2025-08-31 | 04:30 EST | By: Claude-3.5]

**VERSION HISTORY:**
- v2.0 (2025-08-31): Complete rewrite with numbered rules, templates, validator script
- v1.0 (2025-08-31): Initial version (too vague, deprecated)

**ENFORCEMENT:** Run `python 9--(Helper)_(Scripts)/session_end_validator.py` before ending ANY session

======================================================================
======================================================================








# CRITICAL: FILES TO GIVE NEW AGENTS

When onboarding a new agent, provide ONLY these files in this order:
1. `0.2--(Project)_(Overview)_(Current)_(State)` - Current snapshot
2. THIS FILE - Contribution rules
3. Work files specified in Project Overview's "ACTIVE WORK FILE" section

DO NOT give them README files - they auto-update those, not read them.


======================================================================
======================================================================








# SECTION 1: TIME STAMP FORMATS (MANDATORY)

## §1.1 Work Session Time Stamps
**TEMPLATE:** `[YYYY-MM-DD | HH:MM-HH:MM EST | Agent-Version]`

**GOOD EXAMPLE:** `[2025-08-31 | 14:30-16:45 EST | Claude-3.5]`
**BAD EXAMPLE:** `[Aug 31 | afternoon | Claude]`

## §1.2 Single Action Time Stamps  
**TEMPLATE:** `[YYYY-MM-DD | HH:MM EST | Agent-Version]`

**GOOD EXAMPLE:** `[2025-08-31 | 14:30 EST | GPT-4]`
**BAD EXAMPLE:** `[2025-08-31 | 2:30 | GPT]`

## §1.3 Agent Name Format
**ALLOWED FORMATS:**
- `Claude-3.5`
- `GPT-4`
- `Claude-3.5-Sonnet`
- `GPT-4-Turbo`

**NOT ALLOWED:** `Claude`, `ChatGPT`, `Assistant`


======================================================================
======================================================================








# SECTION 2: PROJECT OVERVIEW UPDATE RULES

## §2.0 Header Timestamp Update (MANDATORY EVERY SESSION)

**LOCATION:** Line 4 of `0.2--(Project)_(Overview)_(Current)_(State)`

**TEMPLATE:** `[Last Updated: YYYY-MM-DD | HH:MM EST | By: Agent-Version]`

**RULE:** Update this EVERY time you modify the Project Overview file

## §2.1 Short-Term Memory Updates (MANDATORY EVERY SESSION)

**LOCATION:** `0.2--(Project)_(Overview)_(Current)_(State)` → "SHORT-TERM MEMORY" section

**TEMPLATE:**
```
### 📍 Entry [1/2/3] ([Latest/Middle/Oldest]):
[YYYY-MM-DD | HH:MM-HH:MM EST | Agent-Version]
**WHAT:** [One line description]
**WHERE:** [Exact folder/file path]
**RESULT:** [Specific outcome with details]
**NEXT:** [Immediate next action]
```

**RULE:** Maximum 3 entries. When adding 4th, DELETE the oldest.

## §2.2 Current Work Context Updates (MANDATORY EVERY SESSION)

**TEMPLATE:**
```
**PRIMARY WORK FILE:** `NUMBER--(Name)` 
- Full path: `./12--(Progress)_(Tracking)/NUMBER--(Name)/`

**ADDITIONAL CONTEXT NEEDED:** [List files] OR `None currently`

**CURRENT PHASE:** [Exact status]

**NEXT PLANNED WORK:** [Specific next action]
```

## §2.3 Session Insights Updates (ONLY FOR GOTCHAS AND TRAPS)

**LOCATION:** `0.2--(Project)_(Overview)_(Current)_(State)` → "SESSION INSIGHTS" section

**WHEN TO ADD:**
- Discovered a non-obvious workaround or gotcha
- Found something that breaks unexpectedly
- Identified a trap future agents might fall into
- Solved a confusing problem that wasn't documented

**DO NOT ADD:**
- Obvious things ("Docker runs databases" - no shit)
- Normal progress updates (those go in memory)
- Standard procedures (everyone knows how venv works)

**TEMPLATE:**
```
💡 **[Brief descriptive title]**
- [One line explaining the gotcha/issue]
- [One line explaining the fix/workaround]
```

**RULES:**
- These are PERMANENT - never delete
- Keep EXTREMELY brief (2-3 lines max)
- Only add if it would save future agents from confusion
- Focus on the unexpected/non-obvious

## §2.4 Technical Setup Updates (ONLY WHEN ARCHITECTURE CHANGES)

**TRIGGER CONDITIONS:**
- Python version change
- Package added/removed
- Port number change
- File location change
- Docker configuration change

**UPDATE FORMAT:**
```
## Current Dependencies & Infrastructure:
[Section Name] [vNUMBER - Updated YYYY-MM-DD]:
- [Changed items with specifics]

## Version Change Log:
- vNUMBER: [What changed and why]
```


======================================================================
======================================================================








# SECTION 3: WORK FILE ENTRY RULES

## §3.1 When to Create NEW Work File

**CREATE NEW FILE IF:**
1. Starting different TYPE of work (setup → coding → testing)
2. Moving to different COMPONENT (agents → API → orchestrator)
3. Current file exceeds 500 lines
4. Been 7+ days since last entry in existing file

**FILE NAMING:** `NUMBER--(Component)_(Action)_(Phase)`
- GOOD: `2--(Agent)_(Code)_(Creation)`
- BAD: `2--(Work)_(Stuff)`

## §3.2 Work Entry Template (EXACT FORMAT REQUIRED)

```markdown
----------------------------------------------------------------------
### SUBSECTION: [Specific Descriptive Title - Not Generic]
----------------------------------------------------------------------

[YYYY-MM-DD | HH:MM-HH:MM EST | Agent-Version]

**WHAT WE DID:** [One clear sentence]

**DETAILS:**
- [Specific action with full path]
- [Configuration with exact values]
- [Dependencies with versions]

**WHY THIS MATTERS:**
- [Impact on system]
- [Dependencies created]
- [Future implications]

**HOW TO VERIFY/ACCESS:**
```bash
cd /Users/chrishamlin/exact/path
command --with-flags
# Expected output: [what should appear]
```

**SESSION INSIGHTS:** 
💡 **INSIGHT:** [Realization/learning]
📍 **CONTEXT:** [Why this came up]
🔄 **IMPACT:** [What changes because of this]

**FILES CREATED/MODIFIED:**
- `/Users/chrishamlin/.../file.ext` - [Purpose: what it does]
- `/Users/chrishamlin/.../file2.ext` - [Contains: what's in it]
```

## §3.3 Cross-Reference Rule

**IF** work spans multiple components:
**THEN** create entry in EACH relevant file with cross-reference:

```
**SEE ALSO:** Entry in `3--(Other)_(Component)` for related work
```


======================================================================
======================================================================








# SECTION 4: LLM LIMITATIONS TRACKING

## §4.1 Required Categories (MUST BE ONE OF THESE)

1. `Context Window` - Size/retention issues
2. `Memory/State` - Forgetting previous context
3. `Logic/Reasoning` - Incorrect conclusions
4. `Tool Use` - Misusing or failing with tools
5. `Knowledge Cutoff` - Outdated information
6. `Output Format` - Formatting/structure errors
7. `String Processing` - Path/text handling errors

## §4.2 Limitation Entry Template

```markdown
### [Specific Limitation Title]
**Date:** YYYY-MM-DD | HH:MM EST
**Agent:** [Agent-Version]
**Category:** [One from §4.1 list]
**Severity:** [Critical/High/Medium/Low]

**EXPECTED BEHAVIOR:**
[What should have happened]

**ACTUAL BEHAVIOR:**
[What actually happened]

**ROOT CAUSE:**
[Why it happened - be specific]

**WORKAROUND:**
[Exact solution used]

**DETECTION PATTERN:**
[How to identify this in future]
```


======================================================================
======================================================================








# SECTION 5: README UPDATE RULES (PROJECT-WIDE)

## §5.1 Global README Rule

**EVERY** folder in the ENTIRE project with 2+ items MUST have:
`0--(README_Folder)/(README_Folder).md`

## §5.2 Update Triggers

**UPDATE README WHEN:**
- Adding files to folder
- Removing files from folder
- Changing file purposes
- Renaming files
- Changing folder structure

## §5.3 README Template

```markdown
# [Folder Name] - What's In This Folder

[Last Updated: YYYY-MM-DD | HH:MM EST | By: Agent-Version]

## What The Fuck Is This?
[Immediate explanation of folder purpose]

## Contents
- **file1.ext** - [What it does/contains]
- **folder1/** - [What's in there]

## How To Use
[Specific instructions if applicable]
```


======================================================================
======================================================================








# SECTION 6: VALIDATION SCRIPT USAGE

## §6.1 When to Run (MANDATORY)

**RUN BEFORE:** Ending ANY work session
**LOCATION:** `12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/session_end_validator.py`

## §6.2 How to Run

```bash
cd /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)
python 12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/session_end_validator.py
```

## §6.3 Expected Output

**SUCCESS:**
```
✅ VALIDATION PASSED
- Project Overview: Updated within last 2 hours
- Work Files: New entries found
- READMEs: All current
- Session Complete: OK to end
```

**FAILURE:**
```
❌ VALIDATION FAILED
MISSING UPDATES:
- Project Overview: Last updated 3+ hours ago
  FIX: Add entry using template in §2.1
- README out of date: ./folder/0--(README_Folder)
  FIX: Update with current file list
```


======================================================================
======================================================================








# SECTION 7: NUMBERED WORK HISTORY FILE OUTPUT

## §7.1 At Session Start (MANDATORY)

**After reading Project Overview, OUTPUT TO CHRIS:**
```
Numbered work history files I'm accessing:
- /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/1--(PoC)_(Project)_(Setup)/(PoC)_(Project)_(Setup).md
[List ALL numbered history files you're reading - the ones with NUMBER--(Description) format]
```

**WHAT THESE ARE:** The numbered documentation files in the tracking folder like:
- `1--(PoC)_(Project)_(Setup)`
- `2--(Agent)_(Code)_(Creation)` 
- `3--(Orchestrator)_(Development)`
NOT code files, NOT config files - the DOCUMENTATION files that track work done.

## §7.2 At Session End (MANDATORY)

**After updating documentation, OUTPUT TO CHRIS:**
```
Numbered work history files I updated/created:
- /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/1--(PoC)_(Project)_(Setup)/(PoC)_(Project)_(Setup).md
[If you created a NEW numbered file like 2--, list it here with full path]

Numbered work history files the next agent needs:
- /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/[EXACT_FILE(S)]
[List the specific numbered files they'll need - might be just current, might be multiple]
```

**EXAMPLES:**
- Worked on setup only: Output `1--(PoC)_(Project)_(Setup)` path
- Created agent code file: Output `2--(Agent)_(Code)_(Creation)` path 
- Integrated multiple parts: Output all relevant numbered file paths


======================================================================
======================================================================








# SECTION 8: COMMON SCENARIOS WITH EXACT ACTIONS

## §8.1 Scenario: Fixed a Bug

**ACTIONS:**
1. Add entry to relevant work file (§3.2 template)
2. Update Project Overview short-term memory (§2.1)
3. IF LLM-related: Add to LLM Limitations (§4.2)
4. IF created/modified files: Update folder READMEs (§5.2)
5. Run validator script (§6.2)

## §8.2 Scenario: Added New Dependency

**ACTIONS:**
1. Update Project Overview Technical Setup (§2.4)
2. Increment version number
3. Add change log entry with reason
4. Update work file with details
5. Update short-term memory
6. Run validator

## §8.3 Scenario: Starting New Component

**ACTIONS:**
1. Create new numbered work file (§3.1)
2. Update Project Overview "ACTIVE WORK FILE"
3. Add first entry to new work file
4. Update short-term memory
5. Check all READMEs in path
6. Run validator


======================================================================
======================================================================








# SECTION 9: VISUAL FORMATTING REQUIREMENTS

## §9.1 Section Separators

**MAJOR SECTIONS:** 
```
======================================================================
======================================================================
```
With EXACTLY 7 blank lines before and after

**SUBSECTIONS:**
```
----------------------------------------------------------------------
```
With EXACTLY 7 blank lines before and after

## §9.2 Lists and Bullets

**PRIMARY POINTS:** Use bullet `•` or `-`
**SECONDARY POINTS:** Indent with `○` or `-`
**TERTIARY POINTS:** Double indent with `·` or `-`

**EXAMPLE:**
```
• Primary point
  ○ Secondary detail
    · Tertiary information
```


======================================================================
======================================================================








# SECTION 10: IF/THEN DECISION RULES

## §10.1 File Selection Logic

**IF:** Working on same component as previous session
**THEN:** Continue existing work file

**IF:** Starting different type of work
**THEN:** Create new numbered work file

**IF:** Unsure which file to use
**THEN:** Check Project Overview "ACTIVE WORK FILE"

## §10.2 Update Priority Logic

**IF:** Made any code changes
**THEN:** Priority 1: Update work file

**IF:** Session ending
**THEN:** Priority 1: Update Project Overview

**IF:** Found LLM error
**THEN:** Priority 2: Update LLM Limitations

**IF:** Changed folder contents
**THEN:** Priority 3: Update READMEs


======================================================================
======================================================================








# SECTION 11: FORBIDDEN ACTIONS

## ❌ NEVER DO THESE:

1. **Skip timestamp** - EVERY entry needs exact time
2. **Use relative paths** - ALWAYS use absolute paths
3. **Forget timezone** - EST/EDT required
4. **Mix work types** in same file
5. **Keep 4+ memory entries** - Delete oldest
6. **End without validation** - Script is mandatory
7. **Use vague descriptions** - "Fixed stuff" = WRONG
8. **Assume context** - Explain everything
9. **Skip README updates** - Check ALL folders
10. **Interpret rules** - Follow EXACTLY


======================================================================
======================================================================








# SECTION 12: QUICK REFERENCE DATA

## Current Status (UPDATE WHEN CHANGES):
- **Active Work File:** `2--(Documentation)_(Update)_(Fixes)`
- **Next File Number:** `3--`
- **Guidelines Version:** 2.0
- **Validator Script:** `12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/session_end_validator.py`

## Master Paths:
```
Main: /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/
Tracking: ./12--(Progress)_(Tracking)_(What)_(We)_(Did)/
Venv: ./11--(Python)_(Virtual)_(Environment)/venv/
Docker: ./10--(Docker)_(Database)_(Setup)/
```


======================================================================
======================================================================
