-- KDK Sales Chatbot — PostgreSQL setup
-- Run once: psql -U postgres -f db-setup.sql

CREATE DATABASE kdk_chatbot;
\c kdk_chatbot

CREATE TABLE IF NOT EXISTS chat_logs (
  id           SERIAL PRIMARY KEY,
  session_id   VARCHAR(64),
  user_name    VARCHAR(255),
  user_email   VARCHAR(255),
  user_role    VARCHAR(100),
  user_message TEXT NOT NULL,
  bot_response TEXT NOT NULL,
  flagged      BOOLEAN DEFAULT false,
  correction   TEXT,
  created_at   TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_chat_logs_session ON chat_logs (session_id);
CREATE INDEX idx_chat_logs_flagged ON chat_logs (flagged) WHERE flagged = true;
CREATE INDEX idx_chat_logs_created ON chat_logs (created_at DESC);
