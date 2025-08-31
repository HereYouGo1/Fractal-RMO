-- This SQL file sets up your database tables

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- For generating unique IDs

-- Table for AI agents
CREATE TABLE agents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    config JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Table for tasks
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    description TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    result JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- Table for error logs
CREATE TABLE error_logs (
    time TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    task_id UUID,
    agent_id UUID,
    error_type VARCHAR(100),
    message TEXT,
    context JSONB
);

-- Create indexes for faster queries
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_error_logs_type ON error_logs(error_type, time DESC);
