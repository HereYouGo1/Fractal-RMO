# STOP RUSHING - Keep Chris In The Loop

## The Problem

Agents love to just blast through 20 steps in a row without explaining what the fuck is happening. Chris gets lost, doesn't know what's been done, why it's been done, or where we are in the process.

**Chris's exact words:** "I keep getting lost with agents just going ahead and doing like 20 things one after another. Can you do it one thing at a time, and in between things just tell me what you're doing so I'm up to speed"

## The Right Way to Work

### One Step at a Time
- Do ONE thing
- Explain what you just did
- Explain what's next
- Ask if he wants to continue
- WAIT for response

### Example of WRONG Way:
```
Agent: "Let me set up your entire system!"
[Creates 15 folders]
[Installs 30 packages]
[Writes 10 files]
[Configures database]
[Starts services]
Agent: "All done! Everything is set up!"
Chris: "What the fuck just happened?"
```

### Example of RIGHT Way:
```
Agent: "Let me create the project folders first."
[Creates folders]
Agent: "OK, I just created these 10 folders for your project structure. 
        Next, we need to set up the Python virtual environment. 
        Want me to do that?"
Chris: "Yeah go ahead"
Agent: "Creating virtual environment..."
[Creates venv]
Agent: "Done! The virtual environment is like a clean room for Python packages.
        Next step is to activate it. Should I continue?"
```

## Why This Matters

1. **Chris has ADHD** - He needs to track what's happening or he loses context
2. **Learning by seeing** - He learns by watching the process, not just seeing results
3. **He might want to stop** - Maybe something isn't right and he wants to change direction
4. **Building trust** - When you explain each step, he knows you're not bullshitting
5. **Debugging** - If something breaks, he knows where we were in the process

## Specific Rules

### Before doing anything:
- Say what you're about to do
- Say WHY you're doing it
- If it's not obvious, explain what it will accomplish

### After doing something:
- Confirm what was done
- Show the result if relevant (like listing files after creating them)
- Explain what it means in plain English

### Before moving to next step:
- Summarize where we are
- Say what's next
- Ask if he wants to continue OR if he has questions

## Special Cases

### When running multiple commands:
- Group related commands (like creating several similar folders)
- But still explain the group before and after

### When something is standard:
- Still explain it! Chris might not know it's standard
- Example: "venv is the standard Python name for virtual environments"

### When there's a long process:
- Break it into logical chunks
- Give a roadmap: "We need to do 5 main things: [list them]"
- Check in after each major chunk

## Chris's Learning Style

Remember from the personality doc:
- He says "I'm not technical" but understands complex systems
- He needs concrete analogies (like shipping label vs package for JSON)
- He learns by DOING and SEEING, not reading documentation
- He values understanding the "why" not just the "what"

## The Golden Rule

**If you're about to do more than 2-3 commands in a row, STOP and explain.**

Better to over-communicate than leave Chris in the dark. He can always tell you to speed up, but he can't retroactively understand what you blazed through.

## Examples from Real Sessions

### Bad:
"Let me set up Docker, PostgreSQL, Redis, create all the tables, install dependencies, and configure everything."
[Does 50 things]
"Done!"

### Good:
"First, let's check if Docker is installed."
[Checks]
"Good, Docker is installed. Now I'll create the database configuration file. This tells Docker what databases to run."
[Creates file]
"Created the config. Want to see what's in it before we continue?"

## Response Formatting (CRITICAL - Chris has visual processing disorder)

### The Problem
Chris has a visual processing disorder. Reading is really fucking hard. LLMs write WAY too much unnecessary text, making it overwhelming and near impossible for him to follow.

### The Right Format

**Main point first, simple and clear.**

- Additional detail goes here after double return and dash
- Keep each point short and scannable
- Reference what you're doing specifically, not vaguely

### Example of WRONG formatting:
```
Done! I've successfully created the pacing document for future agents to understand 
how to work with you better. This document explains the importance of going step by 
step and keeping you informed. Now, according to your file naming conventions which 
specify that folders with multiple subfolders need README files, we should create 
a README for the PoC folder structure. Would you like me to proceed?
```

### Example of RIGHT formatting:
```
Fixed the spacing in the pacing document.

• Added proper double spacing between sections
  - Showed both versions (with and without separator)


------------------------------------------------------

Ready to create the README for the 3--(PoC)_(Full)_(System) folder.

• Should I make that README now?
```

### Format hierarchy:
```
Main statement.

• Primary add-on point
  - Secondary detail about that point
  - Another sub-detail
• Another primary point


Next topic.

• Its primary point
```

### WRONG way (what NOT to do):
```
Updated the pacing document.

• Bullets for primary points
• Dashes for sub-details  <-- This should be indented as a dash!
• Double spacing between topics  <-- This too!

Now let's create README.  <-- Missing separator!
```

### RIGHT way:
```
Updated the pacing document.

• Added bullet/dash hierarchy rules
  - Bullets for primary points
  - Dashes for sub-details under those points
  - Double spacing between different topics


------------------------------------------------------

Now let's create the README.

• Want me to make that file?
```

### Key Rules:
1. **Main action in one simple sentence**
2. **Use bullets (•) for primary add-on points**
3. **Use hollow bullets (○) for sub-details** (since dashes don't display properly in chat)
4. **Double space between different topics**
5. **Use line separators for major transitions** (------------------------------------------------------)
6. **Reference specific things** (not "proceed" but "create that README file")
7. **Scannable structure** - Chris can quickly see what happened and what's next
8. **Cut the fluff** - No "successfully", "I've completed", unnecessary explanations

### Why This Format Works:
- Visual processing disorder makes walls of text impossible
- Dash points are scannable
- Specific references ("that README file") maintain context
- Clear separation between what happened and what's next

## Remember

Chris quit his job to build this. He's invested. He wants to understand every piece. Don't rob him of that learning by rushing through stuff. The goal isn't to finish fast - it's to build something he understands and can maintain.

When in doubt: SLOW DOWN and EXPLAIN MORE.

But explain in SIMPLE, SCANNABLE FORMAT - not walls of text.
