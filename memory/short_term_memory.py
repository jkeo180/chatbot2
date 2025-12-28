import json
import os
from collections import deque
from typing import Dict, Any, List

MEMORY_FILE = "memory.json"
SHORT_TERM_MAX = 8  # keep last N message pairs (user+assistant)

# Short-term: deque in-memory (not persisted by default)
short_term = deque(maxlen=SHORT_TERM_MAX)

# Long-term: persisted dict
def load_long_term() -> Dict[str, Any]:
    if not os.path.exists(MEMORY_FILE):
        return {"user_facts": {}, "conversations": []}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_long_term(data: Dict[str, Any]) -> None:
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# Short-term API
def add_short_term(role: str, content: str) -> None:
    """Add a message to the short-term rolling memory."""
    short_term.append({"role": role, "content": content})

def get_short_term_messages() -> List[Dict[str,str]]:
    """Return recent short-term messages as a list (oldest -> newest)."""
    return list(short_term)

def clear_short_term() -> None:
    short_term.clear()

# Long-term API
_long_term_cache = None

def get_long_term() -> Dict[str, Any]:
    global _long_term_cache
    if _long_term_cache is None:
        _long_term_cache = load_long_term()
    return _long_term_cache

def persist_long_term() -> None:
    global _long_term_cache
    if _long_term_cache is None:
        return
    save_long_term(_long_term_cache)

def remember_fact(key: str, value: Any) -> None:
    """Save a single user fact (e.g. name, kids, preference)."""
    lt = get_long_term()
    lt.setdefault("user_facts", {})[key] = value
    persist_long_term()

def forget_fact(key: str) -> None:
    lt = get_long_term()
    if "user_facts" in lt and key in lt["user_facts"]:
        lt["user_facts"].pop(key)
        persist_long_term()

def recall_fact(key: str, default=None):
    return get_long_term().get("user_facts", {}).get(key, default)

def append_memory_event(event: Dict[str, Any]) -> None:
    """Append an event to long-term conversation history (optional)."""
    lt = get_long_term()
    lt.setdefault("conversations", []).append(event)
    persist_long_term()
