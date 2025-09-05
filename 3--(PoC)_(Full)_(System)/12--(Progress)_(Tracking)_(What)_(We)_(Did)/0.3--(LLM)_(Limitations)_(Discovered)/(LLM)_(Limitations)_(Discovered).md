# 🔴 LLM LIMITATIONS DISCOVERED
## Ongoing Tracking of Failure Patterns

[Last Updated: 2025-09-05 | 04:45 | By: Claude (User Report)]

======================================================================
======================================================================


# PURPOSE OF THIS DOCUMENT

Track real-world LLM limitations discovered during development. These become data points for the Fractal-RMO system to learn from. Each entry should document:
- What failed
- Why it failed  
- Workaround used
- Pattern to watch for


======================================================================
======================================================================








# LIMITATION ENTRY FORMAT

```
### [Limitation Title]
**Date Discovered:** YYYY-MM-DD
**Agent:** [Which agent found this]
**Category:** [Context Window / Logic / Memory / Tool Use / etc.]

**WHAT HAPPENED:**
[Describe the failure]

**ROOT CAUSE:**
[Why it failed]

**WORKAROUND:**
[How you fixed/avoided it]

**PATTERN:**
[What to watch for in future]
```


======================================================================
======================================================================








# DISCOVERED LIMITATIONS

### Package Compatibility Assumptions
**Date Discovered:** 2025-08-31
**Agent:** Claude
**Category:** Knowledge Cutoff

**WHAT HAPPENED:**
Assumed asyncpg 0.28.0 would work with Python 3.13.7

**ROOT CAUSE:**
LLM training data doesn't include latest compatibility issues. Python 3.13 is newer than training cutoff.

**WORKAROUND:**
Upgraded to asyncpg 0.30.0 after compilation failed

**PATTERN:**
LLMs will suggest package versions from their training data without knowing current compatibility


----------------------------------------------------------------------


### Path Handling with Special Characters
**Date Discovered:** 2025-08-31  
**Agent:** Claude
**Category:** String Processing

**WHAT HAPPENED:**
Paths with parentheses like `11--(Python)_(Virtual)_(Environment)` require quotes in terminal commands

**ROOT CAUSE:**
LLMs often forget shell interprets parentheses as special characters

**WORKAROUND:**
Always quote paths or escape special characters

**PATTERN:**
LLMs generate "clean" commands without considering shell interpretation


----------------------------------------------------------------------


### Context Window Resource Management
**Date Discovered:** 2025-08-31
**Agent:** Claude
**Category:** Context Window

**WHAT HAPPENED:**
Single large documentation file would eventually blow context window

**ROOT CAUSE:**
LLMs don't proactively manage their own context consumption

**WORKAROUND:**
Segment documentation into multiple focused files

**PATTERN:**
LLMs will happily create infinitely growing documents until context fails


----------------------------------------------------------------------


### Working Directory Assumptions
**Date Discovered:** 2025-08-31
**Agent:** Claude  
**Category:** State Management

**WHAT HAPPENED:**
Commands assuming wrong working directory after navigation

**ROOT CAUSE:**
LLMs lose track of current directory state across multiple commands

**WORKAROUND:**
Use absolute paths or explicit `cd` before each operation

**PATTERN:**
LLMs forget stateful changes like directory navigation


----------------------------------------------------------------------


### Incomplete Overwrites in Large Document Updates
**Date Discovered:** 2025-09-05
**Agent:** User Report
**Category:** Large Document Processing

**WHAT HAPPENED:**
When updating large documents (10-20k tokens), LLMs make additive changes without overwriting existing content unless explicitly instructed to replace

**ROOT CAUSE:**
LLMs struggle to maintain comprehensive document awareness at scale. Attention mechanisms can't effectively track all content needing replacement in large contexts (60k+ tokens)

**WORKAROUND:**
- Explicitly specify that content should be overwritten, not just updated
- Use another LLM to review and identify missed overwrites
- Multiple review passes (2+ times) significantly improve accuracy

**PATTERN:**
LLMs default to additive edits rather than replacements in large documents unless given explicit overwrite instructions


----------------------------------------------------------------------


### Cross-Documentation Propagation Failures  
**Date Discovered:** 2025-09-05
**Agent:** User Report
**Category:** Large Document Processing

**WHAT HAPPENED:**
When asked to "put changes in wherever relevant" across large documentation sets, LLMs fail to catch all applicable locations ~90% of the time

**ROOT CAUSE:**
Inability to maintain global awareness across multiple large documents simultaneously. Model attention gets overwhelmed tracking all potential update locations

**WORKAROUND:**
- Pre-scope: Have LLM first identify and list all relevant locations explicitly
- Separate identification from modification into distinct steps
- Focus on "spots that need overwriting" not just "relevant spots"
- Process each identified location individually rather than bulk updates

**PATTERN:**
LLMs rarely achieve perfect comprehensive cross-document updates when context exceeds ~60k tokens. ~90% of the time they miss at least some relevant locations


======================================================================
======================================================================








# PATTERN CATEGORIES EMERGING

## 1. Knowledge Cutoff Issues
- Package versions
- New Python features
- Latest best practices

## 2. Context Management
- Window size limitations
- State tracking across conversation
- File content retention

## 3. Shell/System Interaction  
- Special character handling
- Path interpretation
- Command sequencing

## 4. Assumption Failures
- Environment state
- User's system configuration
- Previous action results

## 5. Large Document Processing
- Incomplete overwrites (additions instead of replacements)
- Cross-documentation propagation failures
- Degraded performance at 60k+ token contexts
- Rarely achieve perfect coverage (~90% of attempts miss some locations)


======================================================================
======================================================================








# NOTES FOR FRACTAL-RMO IMPLEMENTATION

These limitations represent real failure modes to build detection for:

1. **Version Compatibility Checker**
   - Detect when suggesting potentially incompatible versions

2. **Context Window Monitor**
   - Track consumption and warn before overflow

3. **Shell Command Validator**
   - Check for special characters needing escape

4. **State Tracking System**
   - Maintain awareness of directory, environment changes

5. **Document Scope Analyzer**
   - Pre-identify all locations needing updates before execution
   - Separate scoping from modification phases

6. **Multi-Pass Verification System**  
   - Use multiple LLM passes to catch missed updates
   - Second pass specifically checks for incomplete overwrites

7. **Large Document Chunking Strategy**
   - Break documents >10k tokens into manageable segments
   - Process updates segment-by-segment with overlap checks

Each limitation here is a future test case for the system.


======================================================================
======================================================================
