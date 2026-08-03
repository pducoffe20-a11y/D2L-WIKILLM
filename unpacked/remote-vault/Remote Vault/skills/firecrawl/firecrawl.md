# Firecrawl Integration

Firecrawl is configured for this repository to enable web scraping, searching, and interaction with web pages via Claude Code agents.

## Setup

- **Status:** Initialized with global CLI installation
- **Skills Installed:** 32 skills across Claude Code AI agents
  - Core firecrawl skills (10)
  - Skills to build with firecrawl (6)
  - Firecrawl workflow skills (16)

## Available Commands

### Scrape
Extract content from a single webpage:
```bash
firecrawl scrape https://example.com
```

### Search
Search the web for content:
```bash
firecrawl search "your query"
```

### Interact
Control and interact with a live browser session:
```bash
firecrawl interact "action to perform"
```

## Configuration

The Firecrawl API key is authenticated and ready to use. Additional setup options:

- **Add MCP:** `firecrawl setup mcp`
- **Configure defaults:** `firecrawl setup defaults`
- **Make default:** `firecrawl make default`

## Skills Available

Use these skills in Claude Code:
- `firecrawl` — CLI-based scraping and searching
- `firecrawl-agent` — AI-powered structured data extraction
- `firecrawl-build` — Integrate into application code
- `firecrawl-crawl` — Bulk website extraction
- `firecrawl-search` — Web search integration
- And more...

For complete command reference:
```bash
firecrawl --help
```
## See Also

- Firecrawl docs: https://docs.firecrawl.dev
- Claude Code integration: Mention firecrawl in your requests to trigger skill usage
