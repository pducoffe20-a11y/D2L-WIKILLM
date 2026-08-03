---
name: firecrawl
description: Crawl and extract structured data from web pages for sales research, competitive intelligence, and market monitoring
tags:
  - ai/agent-skill
  - skill/category/data-collection
  - resource/tools
  - utility/web-crawling

---

# Firecrawl Web Crawling & Extraction

Firecrawl is a web crawling and data extraction service integrated with Claude Code skills to enable automated collection of web content for research, analysis, and intelligence gathering.

## Core Commands

### 1. Scrape a Single Page
```bash
firecrawl scrape https://example.com [--markdown|--html|--json]
```

Extract content from a single URL with optional format specification (default: markdown).

### 2. Search the Web
```bash
firecrawl search "your search query" [--limit N]
```

Search for web pages matching your criteria and return results with URLs and snippets.

### 3. Interact with Pages
```bash
firecrawl interact "action to perform" [--url URL]
```

Control a live browser to interact with JavaScript-heavy pages.

### 4. Bulk Crawl a Site
```bash
firecrawl crawl https://example.com [--limit N] [--depth D]
```

Crawl an entire website up to specified depth and page limit.

## Usage in D2L Skills

### For Sales Research Workflows
Use firecrawl to gather:
- Current pricing from competitor websites
- Product feature updates and announcements
- Customer success stories and case studies
- Implementation timelines and requirements
- Integration capabilities and API documentation

### For Competitive Intelligence
Extract:
- Company news and press releases
- Product roadmap announcements
- Compliance and security certifications
- Market position and partnership announcements

### For Market Monitoring
Monitor:
- Industry trends and analyst reports
- Customer reviews and G2/Capterra ratings
- Job postings (hiring signals)
- Funding announcements and company growth

## Best Practices

1. **Respect robots.txt**: Check if sites allow crawling before automated extraction
2. **Rate Limiting**: Implement delays between requests to avoid overwhelming servers
3. **Data Licensing**: Verify you have rights to use extracted content
4. **Relevant Context**: Use site context to improve extraction accuracy
5. **Error Handling**: Handle timeouts and extraction failures gracefully

## Output Formats

- **Markdown**: Clean, readable text format (default)
- **HTML**: Raw HTML structure for complex layouts
- **JSON**: Structured data for programmatic processing
- **Structured**: AI-extracted entities and relationships

## Limitations

- JavaScript-heavy sites may require the `interact` command
- Very large sites may need pagination handling
- Protected content (login required) cannot be accessed
- Rate limits apply based on Firecrawl API plan

## Integration with Other Skills

Firecrawl works well with:
- **d2l-brain-search**: Get current web data to supplement vault searches
- **d2l-change-radar**: Monitor competitor and market websites for changes
- **d2l-sales-brief**: Gather current proof points and case studies
- **d2l-proof-finder**: Extract customer testimonials and success metrics

## Configuration

The Firecrawl API key should be configured in your environment:

```bash
export FIRECRAWL_API_KEY="your-api-key-here"
```

Or configure in Claude Code settings:
```json
{
  "env": {
    "FIRECRAWL_API_KEY": "your-api-key-here"
  }
}
```

## Resources

- Firecrawl Documentation: https://docs.firecrawl.dev
- API Reference: https://docs.firecrawl.dev/api-reference
- CLI Guide: https://docs.firecrawl.dev/cli

## Troubleshooting

### Command Not Found
Install firecrawl CLI:
```bash
npm install -g @firecrawl/cli
```

### Authentication Issues
Verify your API key is set and valid:
```bash
firecrawl auth status
```

### Extraction Failures
- Try different format (--markdown vs --html)
- Check if site requires JavaScript rendering
- Verify site is accessible and allows crawling
