"""Shared helpers for preference radar modules."""

from __future__ import annotations

from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    parsed = urlparse(str(url))
    host = parsed.hostname or ""
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path.rstrip("/")
    return f"{host}{path}"
