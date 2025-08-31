# Progress Tracking System - What's In This Folder

[Last Updated: 2025-08-31 | 10:31 PST | By: Claude-4.1-Opus]

======================================================================

## What The Fuck Is This?

This folder contains the COMPLETE documentation system for the Fractal-RMO project. It tracks everything we do, why we do it, and how to continue the work. The system is designed to prevent context window blowout while maintaining comprehensive history.


======================================================================


## Folder Structure & Purpose

### 📋 Meta/System Files (0.x series)
These files tell you HOW to work with the project:

**0--(README_Folder)/** 
- THIS FILE - explains the tracking system
- Always check if this is current when folder contents change

**0.1--(Contribution)_(Guidelines)_(MUST_READ)/**
- THE RULEBOOK - how to document your work
- Contains all auto-contribution rules
- Has examples and templates
- **READ THIS BEFORE DOING ANYTHING**

**0.2--(Project)_(Overview)_(Current)_(State)/**
- LIVING SNAPSHOT of project RIGHT NOW
- What we're working on currently
- Technical setup that exists
- Last 3 work entries (rolling memory)
- Tells you which work files to load for context

**0.3--(LLM)_(Limitations)_(Discovered)/**
- Ongoing list of LLM failures we discover
- Patterns of errors
- Workarounds found

**0.4--(Documentation)_(Validator)_(Script)_(BS)/**
- Contains the validation script for checking documentation updates
- Moved here from helper scripts folder

**0.5--(Documentation)_(Update)_(Prompt)/**
- The correct prompt to give agents for updating documentation
- Has exact file paths and rule references


### 📚 Work History Files (1+ series)
These contain detailed documentation of work done:

**1--(PoC)_(Project)_(Setup)/**
- Everything we did to set up the PoC environment
- Folder structure, venv, dependencies, Docker

**2--(Documentation)_(Update)_(Fixes)/**
- Fixed broken documentation update prompts
- Corrected file paths and naming conventions

**Future numbered files will be created as new major sections begin**
- Example: 3--(Agent)_(Code)_(Creation)
- Example: 4--(Orchestrator)_(Development)
- Each major work section gets its own file


======================================================================


## How To Use This System

### 🆕 If You're a New Agent:
1. Read THIS file (you are here)
2. Read **0.2--(Project)_(Overview)_(Current)_(State)** to understand current status
3. It will tell you which work files to load for full context
4. Read **0.1--(Contribution)_(Guidelines)** to know how to document
5. Continue work and UPDATE the tracking files per guidelines

### 📝 If You're Chris:
- Check **0.2--(Project)_(Overview)** for quick memory refresh
- The short-term memory section shows last 3 things done
- Session insights show important discoveries/decisions
- Current work context shows what file we're actively working in


======================================================================


## Critical Rules

⚠️ **This README must be updated whenever folder structure changes**

⚠️ **Every work session must update the Project Overview file**

⚠️ **New major sections require new numbered work files**

⚠️ **All contributions must follow the guidelines in 0.1**


======================================================================
