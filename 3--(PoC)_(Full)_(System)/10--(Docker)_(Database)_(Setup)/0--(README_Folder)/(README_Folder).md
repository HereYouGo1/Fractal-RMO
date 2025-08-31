# Docker Database Setup - What's In This Folder

[Last Updated: 2025-08-31 | 04:50 PST | By: Claude-3.5]

## What The Fuck Is This?

This folder contains the Docker configuration files for running PostgreSQL and Redis databases in containers. These databases are the backbone of the Fractal-RMO system - PostgreSQL stores all persistent data and Redis handles caching/queuing.

## Contents

- **0--(README_Folder)/** - This file
- **docker-compose.yml** - Main Docker configuration defining both database containers
- **init.sql** - SQL script that creates initial database tables when PostgreSQL starts

## How To Use

1. Make sure Docker Desktop is running

2. Start databases:
   ```bash
   cd /Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/10--(Docker)_(Database)_(Setup)
   export $(cat ../.env | grep -v '^#' | xargs)
   docker-compose up -d
   ```

3. Check they're running:
   ```bash
   docker ps
   ```

4. Stop databases:
   ```bash
   docker-compose stop
   ```

5. Delete everything (fresh start):
   ```bash
   docker-compose down -v
   ```

## Current Status

✅ Both databases configured and running
- PostgreSQL on port 5432
- Redis on port 6379
