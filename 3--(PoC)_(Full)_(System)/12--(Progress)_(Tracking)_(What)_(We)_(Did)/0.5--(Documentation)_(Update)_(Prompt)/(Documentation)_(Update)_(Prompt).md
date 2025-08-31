# 🚨 MANDATORY DOCUMENTATION UPDATE - DO THIS NOW 🚨

**You MUST update project documentation before continuing or ending this session.**
**Skipping these steps will break project continuity.**

**Current Working Directory:** `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/`

======================================================================

## STEP 1: READ THE CONTRIBUTION GUIDELINES (DO NOT SKIP)

**Read this file FIRST - it contains all numbered rules (§1.1, §2.1, etc.) you must follow:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.1--(Contribution)_(Guidelines)_(MUST_READ)/(Contribution)_(Guidelines)_(MUST_READ).md
```

**Then check the current project state to see what work file is active:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Project)_(Overview)_(Current)_(State)/(Project)_(Overview)_(Current)_(State).md
```

Look for the **"CURRENT WORK CONTEXT"** section → **"PRIMARY WORK FILE"** to know which numbered file to update.

**IMPORTANT:** If you're starting a NEW type of work (different component/phase), you'll create a new numbered file in Step 3 instead of updating the existing one.

======================================================================

## STEP 2: UPDATE PROJECT OVERVIEW (Follow Rules §2.1 and §2.2)

**File to update:**
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Project)_(Overview)_(Current)_(State)/(Project)_(Overview)_(Current)_(State).md
```

**Required updates:**

### A. SHORT-TERM MEMORY section - Follow §2.1 template EXACTLY:
- Add your work as new Entry 3 (Latest)
- Move old Entry 3 → Entry 2
- Move old Entry 2 → Entry 1 
- DELETE the old Entry 1 (oldest - keep maximum 3 entries)

### B. CURRENT WORK CONTEXT section - Follow §2.2 template EXACTLY:
- Update **PRIMARY WORK FILE** if you created a new numbered file
- Update **CURRENT PHASE** with what you just completed
- Update **NEXT PLANNED WORK** with the immediate next action

======================================================================

## STEP 3: UPDATE WORK HISTORY FILE (Follow Rules §3.1 and §3.2)

**Check Project Overview for the PRIMARY WORK FILE path.**

Common work files:
- `1--(PoC)_(Project)_(Setup)/(PoC)_(Project)_(Setup).md` - For environment/setup work
- `2--(Agent)_(Code)_(Creation)/(Agent)_(Code)_(Creation).md` - For agent development
- `3--(Orchestrator)_(Development)/(Orchestrator)_(Development).md` - For orchestrator work

### IF continuing existing work:
Add entry to the existing file using §3.2 template

### IF starting NEW type of work (per §3.1 rules):
Create new numbered file like `2--(Component)_(Action)/(Component)_(Action).md`

**Entry Template (from §3.2):**
```markdown
----------------------------------------------------------------------
### SUBSECTION: [Specific Descriptive Title]
----------------------------------------------------------------------

[YYYY-MM-DD | HH:MM-HH:MM PST | Agent-Version]

**WHAT WE DID:** [One clear sentence]

**DETAILS:**
- [Specific action with full path]
- [Configuration with exact values]
- [Dependencies with versions]

**WHY THIS MATTERS:**
- [Impact on system]
- [Dependencies created]

**HOW TO VERIFY/ACCESS:**
```bash
cd /Users/chrishamlin/exact/path
command --with-flags
# Expected output: [what should appear]
```

**FILES CREATED/MODIFIED:**
- `/Users/chrishamlin/.../file.ext` - [Purpose: what it does]
```

======================================================================

## STEP 4: UPDATE READMEs IF NEEDED (Follow Rule §5.1)

**IF you added/modified files in any folder**, update that folder's README:
- Check if folder has `0--(README_Folder)/(README_Folder).md`
- If missing and folder has 2+ items, CREATE it
- Update file list and descriptions

======================================================================

## STEP 5: RUN VALIDATOR (Follow Rule §6.2)

**Execute this command (DO NOT SKIP):**
```bash
cd /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)
python 12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/session_end_validator.py
```

**Fix any issues it reports before proceeding.**

======================================================================

## STEP 6: OUTPUT SUMMARY (Follow Rule §7.2)

**You MUST output this exact format:**

```
DOCUMENTATION UPDATES COMPLETED:

Numbered work history files I updated/created:
- /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/[NUMBER]--(Name)/(Name).md - [Added entry/Created new file]

Project Overview sections updated:
- SHORT-TERM MEMORY: Added Entry 3 about [topic]
- CURRENT WORK CONTEXT: Updated to show [current state]

READMEs updated (if any):
- [List any README files you updated]

Validation Status: [PASSED/FAILED with any errors]

Numbered work history files the next agent needs:
- /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/[EXACT FILE(S) THEY NEED]
```

======================================================================

# FOR CHRIS - Quick Reference

## When to use this prompt:
- **Every session end** - No exceptions
- **Major task completion** - After finishing a component
- **Before switching agents** - For clean handoff
- **After significant changes** - New dependencies, architecture changes

## Red flags that agent fucked up:
- Wrong file paths (like 001_PROJECT_OVERVIEW.md instead of actual names)
- Missing timestamps or wrong format (needs YYYY-MM-DD | HH:MM PST | Agent-Version)
- Didn't run validator
- Created files with wrong naming convention
- Skipped updating Project Overview

## If agent skips or fucks up:
```
You didn't follow the documentation update rules. Specifically, you missed [thing].
Per contribution guidelines §[rule number], you must [requirement].
Do it now and show me the exact changes.
```

## Quick verification commands:
```bash
# Check recent file modifications
ls -lat /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/*.md | head -5

# Run validator yourself
python /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.4--(Documentation)_(Validator)_(Script)_(BS)/session_end_validator.py

# Check if Project Overview was updated
head -n 200 /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/12--(Progress)_(Tracking)_(What)_(We)_(Did)/0.2--(Project)_(Overview)_(Current)_(State)/(Project)_(Overview)_(Current)_(State).md | grep -A 10 "Entry 3"
```

## Common agent fuck-ups:
1. **Creates new files instead of updating existing** - Tell them to UPDATE not CREATE
2. **Wrong timestamp format** - Must be [YYYY-MM-DD | HH:MM-HH:MM PST | Agent-Version]
3. **Forgets to delete old memory entry** - Maximum 3 entries, delete oldest
4. **Skips validator** - Make them run it, no exceptions
5. **Uses wrong paths** - All docs are in 12--(Progress)_(Tracking)_(What)_(We)_(Did)/

---

**This prompt replaces the broken UNIVERSAL_DOCUMENTATION_UPDATE_PROMPT.md that had wrong file paths.**
