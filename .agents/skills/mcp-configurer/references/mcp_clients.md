# MCP Clients Reference

Approved MCP servers:

- `context7`: current coding documentation and library/API lookup.
- `github`: repository, issue, and pull request context.
- `huggingface`: models, datasets, papers, Spaces, and Hub tooling.
- `playwright`: browser automation and UI verification.

If a PyTorch-specific MCP server is not verified, use official PyTorch documentation directly.

## Codex

Edit `.codex/config.toml`.

Example:

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

## Cursor

Edit `.cursor/mcp.json`.

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${env:GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

For Hugging Face, use the client-specific snippet from [Hugging Face MCP settings](https://huggingface.co/settings/mcp).

## Claude Code

Use `claude mcp add` or `.mcp.json` / `~/.claude.json`.

```bash
claude mcp add --transport stdio context7 -- npx -y @upstash/context7-mcp
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer $GITHUB_PERSONAL_ACCESS_TOKEN"
claude mcp add --transport stdio playwright -- npx -y @playwright/mcp@latest
```

For Hugging Face, use the client-specific snippet from [Hugging Face MCP settings](https://huggingface.co/settings/mcp).

## Gemini CLI

Edit `.gemini/settings.json`.

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

For Hugging Face, use the client-specific snippet from [Hugging Face MCP settings](https://huggingface.co/settings/mcp).

## Antigravity

Edit `~/.gemini/antigravity/mcp_config.json`.

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "github": {
      "serverUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

For Hugging Face, use the client-specific snippet from [Hugging Face MCP settings](https://huggingface.co/settings/mcp).
