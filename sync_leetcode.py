#!/usr/bin/env python3
"""
Syncs ALL LeetCode submissions (accepted and unsuccessful) into a GitHub repo.

Unlike joshcai/leetcode-sync (which only keeps Accepted runs), this script
writes every submission into a per-problem subfolder, named by timestamp and
status, so you get the full attempt history in one place.

Env vars required:
  LEETCODE_SESSION      - value of the LEETCODE_SESSION cookie
  LEETCODE_CSRF_TOKEN   - value of the csrftoken cookie
Optional:
  DESTINATION_FOLDER    - folder to write into (default: "Solutions")
  STATE_FILE            - path to the JSON file tracking synced submission ids
                           (default: "<DESTINATION_FOLDER>/.sync_state.json")
"""

import json
import os
import re
import time
from datetime import datetime, timezone

import requests

LEETCODE_SESSION = os.environ["LEETCODE_SESSION"]
CSRF_TOKEN = os.environ["LEETCODE_CSRF_TOKEN"]
DEST_FOLDER = os.environ.get("DESTINATION_FOLDER", "Solutions")
STATE_FILE = os.environ.get("STATE_FILE", os.path.join(DEST_FOLDER, ".sync_state.json"))

BASE_URL = "https://leetcode.com/api/submissions/"

LANG_EXT = {
    "python": "py",
    "python3": "py",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "kotlin": "kt",
    "swift": "swift",
    "golang": "go",
    "ruby": "rb",
    "scala": "scala",
    "rust": "rs",
    "php": "php",
    "erlang": "erl",
    "elixir": "ex",
    "dart": "dart",
    "racket": "rkt",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
}


def sanitize(name: str) -> str:
    name = name.strip().replace(" ", "_")
    return re.sub(r"[^A-Za-z0-9_.-]", "", name)


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_state(seen_ids):
    os.makedirs(os.path.dirname(STATE_FILE) or ".", exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(sorted(seen_ids), f, indent=2)


def fetch_all_submissions(session: requests.Session):
    """Yield every submission dict, newest first, across all pages."""
    offset = 0
    limit = 20
    while True:
        resp = session.get(
            BASE_URL,
            params={"offset": offset, "limit": limit},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        submissions = data.get("submissions_dump", [])
        if not submissions:
            break
        for sub in submissions:
            yield sub
        if not data.get("has_next"):
            break
        offset += limit
        time.sleep(1)  # be polite to LeetCode's API


def main():
    session = requests.Session()
    session.cookies.set("LEETCODE_SESSION", LEETCODE_SESSION, domain="leetcode.com")
    session.cookies.set("csrftoken", CSRF_TOKEN, domain="leetcode.com")
    session.headers.update(
        {
            "Referer": "https://leetcode.com/",
            "x-csrftoken": CSRF_TOKEN,
            "User-Agent": "Mozilla/5.0 (compatible; leetcode-full-sync/1.0)",
        }
    )

    seen_ids = load_state()
    new_count = 0

    for sub in fetch_all_submissions(session):
        sub_id = str(sub.get("id"))
        if sub_id in seen_ids:
            # Submissions come back newest-first; once we hit one we've
            # already synced, everything after it is old too.
            break

        title_slug = sub.get("title_slug") or sanitize(sub.get("title", "unknown"))
        status = sanitize(sub.get("status_display", "Unknown"))
        lang = sub.get("lang", "txt")
        ext = LANG_EXT.get(lang, lang)
        ts = int(sub.get("timestamp", time.time()))
        dt = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d_%H%M%S")

        problem_dir = os.path.join(DEST_FOLDER, title_slug)
        os.makedirs(problem_dir, exist_ok=True)

        filename = f"{dt}_{status}.{ext}"
        filepath = os.path.join(problem_dir, filename)

        code = sub.get("code", "")
        header = (
            f"# Problem: {sub.get('title', title_slug)}\n"
            f"# Status: {sub.get('status_display')}\n"
            f"# Language: {lang}\n"
            f"# Runtime: {sub.get('runtime', 'N/A')}\n"
            f"# Memory: {sub.get('memory', 'N/A')}\n"
            f"# Submitted: {dt} UTC\n"
            f"# URL: https://leetcode.com{sub.get('url', '')}\n\n"
        )

        with open(filepath, "w") as f:
            f.write(header + code)

        seen_ids.add(sub_id)
        new_count += 1

    save_state(seen_ids)
    print(f"Synced {new_count} new submission(s).")


if __name__ == "__main__":
    main()
