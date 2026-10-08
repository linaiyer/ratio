#!/usr/bin/env python3
"""Compare an Instagram data export's followers and following lists.

Usage:
    python3 ratio.py FOLLOWERS FOLLOWING

FOLLOWERS / FOLLOWING are the files from the export's
connections/followers_and_following/ folder (followers_1.html and
following.html). JSON exports work too. If you have several followers
files (followers_1, followers_2, ...), pass a comma-separated list.
"""
import json
import re
import sys
from pathlib import Path

# Matches https://www.instagram.com/<user> and https://www.instagram.com/_u/<user>
PROFILE_URL = re.compile(r"https?://(?:www\.)?instagram\.com/(?:_u/)?([A-Za-z0-9._]+)")


def usernames_from_json(data):
    """Collect usernames from Instagram's JSON export shape (any nesting)."""
    found = set()
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "href" and isinstance(value, str):
                m = PROFILE_URL.search(value)
                if m:
                    found.add(m.group(1).lower())
            elif key in ("value", "title") and isinstance(value, str) and value:
                found.add(value.lower())
            else:
                found |= usernames_from_json(value)
    elif isinstance(data, list):
        for item in data:
            found |= usernames_from_json(item)
    return found


def load_usernames(paths):
    names = set()
    for path in paths.split(","):
        text = Path(path.strip()).expanduser().read_text(encoding="utf-8")
        if path.strip().lower().endswith(".json"):
            names |= usernames_from_json(json.loads(text))
        else:
            names |= {m.lower() for m in PROFILE_URL.findall(text)}
    return names


def print_list(title, names):
    print(f"\n{title} ({len(names)})")
    print("-" * (len(title) + len(str(len(names))) + 3))
    for name in sorted(names):
        print(f"  {name}  https://www.instagram.com/{name}")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    followers = load_usernames(sys.argv[1])
    following = load_usernames(sys.argv[2])

    print(f"Followers: {len(followers)}   Following: {len(following)}")
    print_list("Don't follow you back (you follow them)", following - followers)
    print_list("You don't follow back (they follow you)", followers - following)


if __name__ == "__main__":
    main()
