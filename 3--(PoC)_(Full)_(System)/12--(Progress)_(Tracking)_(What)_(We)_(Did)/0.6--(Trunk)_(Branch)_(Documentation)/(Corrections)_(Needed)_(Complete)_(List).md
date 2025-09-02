# COMPLETE LIST OF CORRECTIONS NEEDED
## All Updates Required for Trunk-Branch Documentation

[Created: 2025-09-01 | 09:15 EST | By: Claude-4.1-Opus]

------------------------------------------------------

## KEY DECISIONS FROM OUR CONVERSATION

### Confirmed Decisions to Implement:

1. **Branch Depth:** Maximum 2 levels (Main → Sub), no A-1-a sub-sub-branches
2. **Branch Scope:** Based on deliverables NOT tokens
   - Main branches = Major system components/domains
   - Sub-branches = Specific deliverables within domain
3. **Master Timestamp Log:** Single file replaces ALL individual branch timestamp logs
4. **Dependency Chains:** With lazy update strategy (Chris's E7→A6→C4 example)
5. **Sub-Branch Propositions:** New 0.2 position in main branches for proposed work
6. **Folder Name:** `0.2--(Trunk)_(Branch)_(System)` with underscores
7. **Work Continuation:** Continue in same sub-branch for related work
8. **Multiple Agents:** Can work in same sub-branch across sessions
9. **Branch Updates:** Can update any branch anytime (with cascade checking)
10. **Update Manifest:** Alert list when active branches affected
11. **Git Prompts:** After EVERY update (Chris doesn't know git well)
12. **Branch Creation:** Agents propose in sheet, Chris decides during planning

------------------------------------------------------

## CORRECTIONS BY DOCUMENT

### Architecture Doc (`(Trunk)_(Branch)_(System)_(Architecture).md`)

**MUST FIX:**
- Remove ALL token-based sections completely (not just modify)
- Ensure dependency chain section uses exact E7→A6→C4 example throughout
- Clarify update agent needs only O-F files, not full context
- Add more emphasis on branches remaining after merge

**MUST ADD:**
- Explanation that sub-branch scope = deliverable completion
- Note about multiple agents working in same sub-branch

### Structure Doc (`(Trunk)_(Branch)_(Complete)_(Structure).md`)

**MUST FIX:**
- ALL instances of `0.2--(O-F)` → `0.2--(Trunk)_(Branch)_(System)`
- Index paths: trunk has `(Index)_(Main_Bnchs)` not `(Index)_(Sub-Bnchs)`
- Remove timestamp log from validation rules
- Directory creation commands to exclude timestamp folders

**MUST ADD:**
- Sub-branch propositions format with 4-5 sentence explanations
- Master timestamp log lists ALL sub-branches in order (A-1, A-2... B-1, B-2...)
- Exhaustive explanations per documentation protocol

### Operations Manual (`(Trunk)_(Branch)_(Operations)_(Manual).md`)

**MUST FIX:**
- Replace ALL individual timestamp log references with master log
- Remove token calculation sections
- Update branch creation to be deliverable-based

**MUST ADD:**
- Complete dependency chain checking procedure on login
- Lazy update strategy explanation
- Sub-branch propositions workflow
- Git prompt after EVERY update requirement
- Blocked message format when dependencies outdated

### Advanced Systems Doc (`(Trunk)_(Branch)_(Advanced)_(Systems).md`)

**MUST FIX:**
- Sync agent to use master timestamp log
- Remove ALL token limit references
- Resolve branch creation authority as "propose then decide"

**MUST ADD:**
- Expand E7→A6→C4 example throughout
- Update agent role for bulk O-F updates
- Check-off system details for sync agent

------------------------------------------------------

## EXHAUSTIVE DOCUMENTATION REQUIREMENTS

Per Chris's documentation protocol, EVERY update must:

1. **Define before using** - Explain what O-F means, what trunk is, etc.
2. **Show expected output** - What agents see when blocked, what logs look like
3. **Explain why it matters** - Why lazy updates save time, why master log is better
4. **Include recovery steps** - If dependency chain breaks, how to fix
5. **Never skip obvious things** - Even "press Enter" needs to be said

------------------------------------------------------

## GLOBAL SEARCH/REPLACE NEEDED

Search for and fix ALL instances of:
- `0.2--(O-F)` → `0.2--(Trunk)_(Branch)_(System)`
- `token` → Remove or replace with deliverable-based explanation
- `Timestamp)_(Update)_(Log)` → Replace with master timestamp log
- Incorrect index references

------------------------------------------------------

## FORMAT REQUIREMENTS

Per Chris's preferences:
- Main point first, simple and clear
- Bullet points for additional details
- Double spacing between topics
- Line separators for major transitions
- Reference specific things, not vague terms

------------------------------------------------------

## VALIDATION CHECKLIST

Before finalizing:
- [ ] All folder names have underscores between words
- [ ] No token-based decisions remain
- [ ] Master timestamp log fully explained
- [ ] Dependency chains with E7 example clear
- [ ] Sub-branch propositions documented
- [ ] Git prompts mentioned throughout
- [ ] Exhaustive explanations provided
- [ ] All paths are absolute and correct
- [ ] Revision timestamps updated

------------------------------------------------------

## WHY THIS MATTERS

Chris quit his job to build Fractal-RMO. These documents are the foundation for parallel development without conflicts. Every error compounds across agents. Get it right once.

======================================================================
======================================================================
