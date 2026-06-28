# MCP usage policy

Use approved MCP servers when they provide fresher or more authoritative context than model memory.

For code, SDK, library, or API tasks, prefer Context7 MCP before making implementation changes when the server is configured and available.

Use GitHub MCP for repository, issue, and pull request context; use Hugging Face MCP for model, dataset, paper, and Space lookup; use Playwright MCP for browser-level verification and UI interaction.

For non-Codex clients, mirror the same approved server set in the client's native MCP config file; `mcp-configurer` and its `references/mcp_clients.md` file are the repo reference for the supported file paths and syntax.

Use the `mcp-configurer` skill when setting up or auditing MCP client configuration.

If a PyTorch-specific MCP server is not configured, use official PyTorch documentation or the repository source directly instead of inventing one.

If MCP output materially affects a code or documentation decision, record the relevant source, version, or API details in the task artifacts. If the information is external evidence rather than transient implementation guidance, save the durable note under `sources/` when appropriate.

If MCP is unavailable, fall back to official documentation and state the fallback explicitly.