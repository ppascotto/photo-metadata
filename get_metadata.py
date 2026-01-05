#!/usr/bin/env python3

import os
import json
import shutil
from datetime import datetime, timezone
import cleanup

OUTPUT_DIR = "Output"


def datetime_from_json(data):
    if "photoTakenTime" in data:
        ts = int(data["photoTakenTime"]["timestamp"])
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    return None


def safe_copy(src, dst):
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
        return dst

    base, ext = os.path.splitext(dst)
    i = 1
    while True:
        candidate = f"{base}_{i}{ext}"
        if not os.path.exists(candidate):
            shutil.copy2(src, candidate)
            return candidate
        i += 1


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in sorted(os.listdir(".")):
        if not filename.lower().endswith(".json"):
            continue

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        dt = datetime_from_json(data)
        if not dt:
            print(f"Skipping {filename}: no photoTakenTime")
            continue

        title = data.get("title")
        if not title:
            print(f"Skipping {filename}: no title field")
            continue

        src = title
        if not os.path.exists(src):
            print(f"Media file not found for {filename}: {src}")
            continue

        ext = os.path.splitext(src)[1].lower()
        name = dt.strftime("%Y%m%d_%H%M%S") + ext
        dst = os.path.join(OUTPUT_DIR, name)

        safe_copy(src, dst)


if __name__ == "__main__":
    main()
