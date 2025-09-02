# VISUAL DOCUMENTATION STANDARDS
## How to Create Clean, Professional Visual Documentation

[Created: 2025-09-01 | 22:15 EST | By: Claude-4.1-Opus]
[Purpose: Universal guide for all agents creating visual documentation]


------------------------------------------------------

## What The Fuck Is This?

This guide teaches you how to create clean, aligned, professional visual documentation that Chris can actually read and understand.

• **Problem:** Most agents create messy boxes with misaligned sides
• **Solution:** Use proper box-drawing characters and counting techniques
• **Result:** Clean, scannable visuals that support Chris's ADHD and visual processing needs


------------------------------------------------------

## 📦 BOX DRAWING TOOLKIT
### Copy-Paste These Characters

**Box Components:**
```
Corners:  ┌ ┐ └ ┘
Lines:    ─ │ ═ ║
Junctions: ├ ┤ ┬ ┴ ┼
Arrows:   → ← ↑ ↓ ↔ ⇒ ⇐
Special:  ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
```

**Complete Box Example:**
```
┌─────────────────┐
│   Clean Box     │
├─────────────────┤
│ • Aligned sides │
│ • Clear content │
└─────────────────┘
```

**ASCII Fallback (if Unicode unavailable):**
```
+------------------+
|   Fallback Box   |
+------------------+
| - Still aligned  |
| - Less pretty    |
+------------------+
```


------------------------------------------------------

## ⚖️ ALIGNMENT RULES
### The Secret to Clean Boxes

**Rule 1: Count Characters**
```
WRONG (misaligned):
┌──────┐
│ A │
└──────┘
    ┌────────┐
    │ B-1 │
    └────────┘

RIGHT (aligned):
┌─────────┐
│    A    │
└─────────┘
┌─────────┐
│   B-1   │
└─────────┘
```

**Rule 2: Use Monospace Awareness**
• Every character occupies exactly one column
• Count spaces carefully
• Test alignment in a monospace font

**Rule 3: Vertical Consistency**
```
┌─────────┐     ┌─────────┐
│ Box One │────►│ Box Two │
└─────────┘     └─────────┘
     │               │
     ▼               ▼
┌─────────┐     ┌─────────┐
│  Three  │     │  Four   │
└─────────┘     └─────────┘
```


------------------------------------------------------

## 📊 VISUAL HIERARCHY PRINCIPLES

### Layer Your Information
```
Layer 1: Overview (bird's eye view)
     ↓
Layer 2: Main Components
     ↓
Layer 3: Details
     ↓
Layer 4: Examples
```

### Use Visual Breathing Room
```
WRONG (cramped):
Section 1
Section 2
Section 3

RIGHT (breathable):
Section 1

Section 2

Section 3
```

### Employ Clear Separators
```
Major sections:
======================================================================

Minor sections:
------------------------------------------------------

Inline breaks:
──────────
```


------------------------------------------------------

## ❌ COMMON MISTAKES & FIXES

### Mistake 1: Inconsistent Box Characters
```
WRONG:
+---┐
| A |
└---+

RIGHT:
┌───┐
│ A │
└───┘
```

### Mistake 2: Wall of Text in Diagrams
```
WRONG:
┌────────────────────────────────────┐
│ This box contains way too much     │
│ text and becomes unreadable when   │
│ you try to cram everything into    │
│ one place without any structure    │
└────────────────────────────────────┘

RIGHT:
┌─────────────┐
│  Main Idea  │
└──────┬──────┘
       │
   ┌───▼───┐
   │Details│→ [See explanation below]
   └───────┘
```

### Mistake 3: No Flow Direction
```
WRONG:
[A] [B] [C]
[D] [E] [F]

RIGHT:
A → B → C
↓       ↓
D → E → F
```


------------------------------------------------------

## 🎯 WHEN TO USE VISUALS

### Use Diagrams For:
• System architecture
• Process flows
• Hierarchical relationships
• State transitions
• Dependency chains

### Use Lists For:
• Sequential steps
• Feature enumerations
• Simple comparisons
• Quick references

### Use Tables For:
• Multi-dimensional comparisons
• Data with consistent structure
• Configuration mappings


------------------------------------------------------

## 🏆 GOOD VS BAD EXAMPLE

### BAD Visual:
```
system overview
+--trunk--+
|overview file|
+--+
  |__ branch a
    |_subbranch a1
    |_subbranch a2
  |__ branch b
```

### GOOD Visual:
```
SYSTEM OVERVIEW
===============

      ┌────────────┐
      │   TRUNK    │
      │  (Truth)   │
      └─────┬──────┘
            │
    ┌───────┴───────┐
    ▼               ▼
┌────────┐     ┌────────┐
│Branch A│     │Branch B│
└───┬────┘     └───┬────┘
    │              │
  ┌─┴─┐          ┌─┴─┐
  │A-1│          │B-1│
  └───┘          └───┘
```

**What Changed:**
• Proper box characters
• Clear hierarchy
• Aligned elements
• Visual flow
• Descriptive title


------------------------------------------------------

## 🧠 CHRIS'S SPECIFIC REQUIREMENTS

### Must-Haves:
• **"What The Fuck Is This?"** section at the top
• **Visual breathing room** between sections
• **Scannable structure** for ADHD support
• **Clear separators** using ====== or ------
• **Progressive disclosure** (overview → details)

### Remember:
• Chris has visual processing disorder
• Clean visuals reduce cognitive load
• Walls of text are impossible for him
• Structure enables comprehension


------------------------------------------------------

## ✅ VISUAL DOCUMENTATION CHECKLIST

Before submitting any visual documentation:

☐ Boxes have clean, aligned vertical sides
☐ Used proper box-drawing characters (or clean ASCII)
☐ Included "What The Fuck Is This?" section
☐ Added visual breathing room between sections
☐ Flow direction is clear (arrows show path)
☐ Information is layered (not all at once)
☐ Tested alignment in monospace font
☐ No walls of text in boxes
☐ Used proper separators between sections
☐ Examples show both good and bad practices


------------------------------------------------------

## 🚀 QUICK REFERENCE

**For Simple Hierarchy:**
```
Parent
├── Child 1
├── Child 2
└── Child 3
```

**For Process Flow:**
```
Start → Process → Decision → End
           ↓
        Alternative
```

**For State Diagram:**
```
┌─────┐  event  ┌─────┐
│State├────────►│State│
│  A  │         │  B  │
└─────┘         └─────┘
```


------------------------------------------------------

## Final Note

These are foundations, not rigid rules. Adapt as needed, but always maintain:
• **Clarity** - Can Chris understand it immediately?
• **Scannability** - Can he find information quickly?
• **Professionalism** - Does it look clean and intentional?

When in doubt, choose clarity over complexity. The goal is communication, not art.


======================================================================
