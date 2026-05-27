---
name: mcp-configurer
description: Configure approved MCP servers across Codex, Cursor, Claude Code, Gemini CLI, and Antigravity. Use when setting up, auditing, or updating MCP client configuration, wiring auth env vars, or checking which approved servers belong in a client config.
---

# Mcp Configurer

## Overview

Use this skill to keep the repo's approved MCP server set consistent across clients.

## Quick start

1. Identify the target client.
2. For Codex, edit `.codex/config.toml` directly.
3. For Cursor, Claude Code, Gemini CLI, or Antigravity, use the native MCP config file or CLI command for that client.
4. Use the approved server set only: `context7`, `github`, `huggingface`, and `playwright`.
5. Wire `GITHUB_PERSONAL_ACCESS_TOKEN` and `HF_TOKEN` when the client needs bearer auth.
6. Prefer the client-specific Hugging Face snippet when available.
7. Keep this skill focused on configuration, not on task guidance.

## Codex setup

Use the project-scoped file at `.codex/config.toml`.

Minimal approved example:

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
enabled = true

[mcp_servers.github]
url = "https://api.githubcopilot.com/mcp/"
bearer_token_env_var = "GITHUB_PERSONAL_ACCESS_TOKEN"

[mcp_servers.huggingface]
url = "https://hf.co/mcp"
bearer_token_env_var = "HF_TOKEN"

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest"]
```

## Reference

Read `references/mcp_clients.md` for the client-by-client paths and snippets.
