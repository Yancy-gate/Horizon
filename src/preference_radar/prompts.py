"""Prompts for preference document ingestion."""

PREFERENCE_INGEST_SYSTEM = """You extract structured preference updates from user documents for a personal news radar.

Return JSON only with this shape:
{
  "summary": "one-line description of what was extracted",
  "interests": ["topic or keyword phrases to track"],
  "negative_interests": ["topics to downrank"],
  "raw_keywords": ["short matching keywords"],
  "google_news_queries": [
    {"query": "search query string", "language": "zh|en", "country": "CN|US", "max_results": 20}
  ],
  "persona_summary_append": "optional sentence to append to persona summary"
}

Rules:
- Prefer concise, searchable phrases over vague themes.
- google_news_queries should be tight (high precision), not broad catch-alls.
- Do not invent interests unrelated to the document.
- negative_interests only when the document clearly rejects a topic.
"""

PREFERENCE_INGEST_USER = """Document filename: {filename}

Document content:
{content}
"""
