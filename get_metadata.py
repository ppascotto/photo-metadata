#!/usr/bin/env python3

import os
import json
import shutil
from datetime import datetime, timezone

OUTPUT_DIR = "Output"

def get_ext(name):
    if name.casefold().endswith('jpg'):
        return '.jpg'
    elif name.casefold().endswith('mov'):
        return '.mov'
    elif name.casefold().endswith('mp4'):
        return '.mp4'
    elif name.casefold().endswith('heic'):
        return '.HEIC'

def shorten_filename(name, EXT):
    """Remove one character before the extension."""
    if not name.endswith(EXT):
        return None

    base = name[:-len(EXT)]
    if len(base) == 0:
        return None

    return base[:-1] + EXT

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

        EXT = get_ext(title)
        current_name = title
        while current_name:
            if os.path.isfile(current_name):
                src = current_name
                break
            else:
                next_name = shorten_filename(current_name, EXT)
                if next_name == current_name or next_name is None:
                    print('File '+title+' not found')
                    break
            current_name = next_name

        # src = title
        # if not os.path.exists(src):
        #     print(f"Media file not found for {filename}: {src}")
        #     continue

        ext = os.path.splitext(src)[1].lower()
        name = dt.strftime("%Y%m%d_%H%M%S") + ext
        dst = os.path.join(OUTPUT_DIR, name)

        safe_copy(src, dst)

if __name__ == "__main__":
    main()
