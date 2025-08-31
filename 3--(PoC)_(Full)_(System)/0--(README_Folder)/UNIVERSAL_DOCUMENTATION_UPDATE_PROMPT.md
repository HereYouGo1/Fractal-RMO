# Universal Documentation Update Prompt for Agents

**CRITICAL DOCUMENTATION UPDATE REQUIRED**

You must now update all project documentation according to the contribution guidelines. This is MANDATORY before proceeding or ending the session.

## STEP 1: Read These Files First (even if you have in the past, do it again incase a different agent running paralell updated them since you last saw them)
```
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/002_CONTRIBUTION_GUIDELINES.md
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/001_PROJECT_OVERVIEW.md
/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/003_LLM_LIMITATIONS.md
```

## STEP 2: List Your Work Files
Output the EXACT paths of all numbered work history files you are working with:
- Your primary work file: `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/00X_PROJECT_WORK_[YourAgentName]_[YYYY-MM-DD].md`
- Any other numbered files you've referenced or need to update

## STEP 3: Update These Documents NOW

### A. Project Overview Updates (001_PROJECT_OVERVIEW.md)
Update these sections with your current work:
- **Section 2.1 (Short-Term Memory)**: Add bullet points for immediate work done
- **Section 2.2 (Current Work Context)**: Update with your active tasks/issues
- **Section 2.3 (Technical Setup)**: Update if you changed any technical configurations

### B. Your Numbered Work History File
File format: `00X_PROJECT_WORK_[YourAgentName]_[YYYY-MM-DD].md`

**IF FILE DOESN'T EXIST**: Create it with next available number (004, 005, etc.)
**IF FILE EXISTS**: Append your new entry

Use this EXACT template for each work entry:
```markdown
## [YYYY-MM-DD HH:MM:SS UTC] - [Your Agent Name]

### Work Performed
- [Specific task 1]
- [Specific task 2]

### Files Modified
- `/path/to/file1.py` - [what changed]
- `/path/to/file2.md` - [what changed]

### Key Decisions
- [Decision 1 and rationale]
- [Decision 2 and rationale]

### Next Steps
- [ ] [Immediate next task]
- [ ] [Follow-up task]

### Notes for Next Agent
[Any critical context or warnings]

---
```

### C. README Updates (if applicable)
**IF you modified files in any folder**, update that folder's README.md:
- Added files → Update file list in README
- Changed functionality → Update description
- New dependencies → Update requirements

Check these README locations based on what you modified:
- Main project root README
- `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/README.md`
- `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/1--(AI)_(Agents)/README.md`
- `/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/2--(Orchestrator)_(Core)/README.md`
- Any other folder where you made changes

### D. LLM Limitations Document (003_LLM_LIMITATIONS.md)
**IF you encountered any errors, bugs, or limitations**, add entry:
```markdown
## [YYYY-MM-DD] - [Error/Limitation Title]
**Agent:** [Your Name]
**Category:** [Language/Memory/Context/Tooling/Logic/Performance]
**Description:** [What happened]
**Impact:** [How it affected work]
**Workaround:** [How you fixed/avoided it]
**Prevention:** [How to prevent in future]
```

## STEP 4: Run Validation Script
Execute this command and fix any issues it reports:
```bash
python /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/9--(Helper)_(Scripts)/session_end_validator.py
```

## STEP 5: Output Your Update Summary

**REQUIRED OUTPUT FORMAT:**
```
DOCUMENTATION UPDATES COMPLETED:

Files I Updated:
1. /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/001_PROJECT_OVERVIEW.md - Sections [list sections]
2. /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/00X_PROJECT_WORK_[AgentName]_[Date].md - [Created/Appended]
3. [Any README files] - [What was updated]
4. [If applicable] /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/003_LLM_LIMITATIONS.md - [Issue added]

Files the Next Agent MUST Read:
1. /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/001_PROJECT_OVERVIEW.md
2. /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/002_CONTRIBUTION_GUIDELINES.md
3. /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/00X_PROJECT_WORK_[YourAgentName]_[YourDate].md
4. [List any other numbered work files relevant to current work]
5. [Any specific source files they need to understand]

Validation Status: [PASSED/FAILED - include any warnings]
```

## STEP 6: Confirm Completion
State: "Documentation updates complete. Ready for [next task/session handoff]."

---

**DO NOT PROCEED WITHOUT COMPLETING ALL ABOVE STEPS**

---

## Additional Notes for Chris

### When to Use This Prompt
- **Mid-session**: When switching major tasks or before a break
- **End-of-session**: Always before ending agent interaction
- **After significant work**: Following any major code changes or discoveries
- **Before handoff**: When preparing to switch to a different agent

### What to Check After Agent Response
1. Verify the agent listed explicit file paths
2. Confirm Project Overview sections were updated
3. Check that numbered work file follows naming convention
4. Ensure timestamp format is correct (YYYY-MM-DD HH:MM:SS UTC)
5. Verify validation script was run

### Quick Validation Commands
After agent completes updates, you can verify:
```bash
# Check if files were modified recently
ls -lat /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/*.md | head -10

# Verify validation script exists and runs
python /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/9--(Helper)_(Scripts)/session_end_validator.py

# Quick check of Project Overview updates
head -50 /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/001_PROJECT_OVERVIEW.md
```

### Red Flags to Watch For
- Agent doesn't provide exact file paths
- Timestamps missing or in wrong format
- No numbered work file created/updated
- Validation script not run
- README updates ignored when folders modified
- LLM limitations not documented when errors occurred

### Template for Follow-up if Needed
If agent misses something:
```
You missed updating [specific file/section]. Per the contribution guidelines section [X], you must [specific requirement]. Please complete this now and show me the exact changes.
```

### Emergency Recovery Commands
If documentation gets corrupted or lost:
```bash
# List all recent modifications
find /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System) -name "*.md" -mtime -1 -ls

# Backup current documentation state
tar -czf docs_backup_$(date +%Y%m%d_%H%M%S).tar.gz /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/

# Check git status for uncommitted changes
git status /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/0--(README_Folder)/
```
