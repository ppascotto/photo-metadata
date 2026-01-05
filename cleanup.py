#!/usr/bin/env python3

import os

def remove_leading_dots():
    for filename in os.listdir("."):
        # Only process files that start with a single leading dot
        if not filename.startswith("."):
            continue

        # Skip special entries like "." and ".." (mostly relevant on Unix)
        if filename in (".", ".."):
            continue

        new_name = filename.lstrip(".")  # remove all leading dots

        # If removing dots results in empty name, skip
        if not new_name:
            print(f"Skipping {filename}: empty result")
            continue

        # Avoid overwriting existing files
        if os.path.exists(new_name):
            print(f"Skipping {filename} → {new_name} (already exists)")
            continue

        os.rename(filename, new_name)
        print(f"Renamed: {filename} → {new_name}")

def cleanup():
    remove_leading_dots()
    print("Scanning directory:", os.getcwd())
    files = os.listdir(".")

    if not files:
        print("Directory is empty.")
        return

    for filename in files:
        print(f"\nFound: {filename}")

        if not filename.lower().endswith(".json"):
            print("  → Skipped (not .json)")
            continue

        stem = filename[:-5]  # remove ".json"
        parts = [p for p in stem.split(".") if p]

        if not parts:
            print("  → Skipped (no valid name parts)")
            continue

        new_name = parts[0] + ".json"

        print(f"  → Proposed new name: {new_name}")

        if filename == new_name:
            print("  → Skipped (already correct)")
            continue

        if os.path.exists(new_name):
            print("  → Skipped (target already exists)")
            continue

        os.rename(filename, new_name)
        print(f"  ✅ Renamed to {new_name}")


if __name__ == "__main__":
    cleanup()
