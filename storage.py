"""
storage.py — Data persistence layer for the Library Management System
=======================================================================

Responsible for reading and writing JSON data files. No other module
should touch the filesystem directly — all data access goes through
this module.

BUILD THIS MODULE FIRST. Nothing else works without save/load.

Why JSON and not a database:
    For a project this size, JSON files are simpler to debug (you can
    open them in any text editor), require no extra dependencies, and
    teach the same persistence concepts. In a real library system,
    you'd use a relational database (PostgreSQL, SQLite) — see stretch goals.

File locations:
    All data files live in the data/ subdirectory, relative to this script.
    Using a subdirectory keeps data files separate from code files.

If You Get Stuck:
    Use an AI assistant to ASK QUESTIONS about concepts — for example:
      "How does os.path.dirname(__file__) work?"
      "What's the difference between json.load and json.loads?"
    DO NOT ask AI to write the solution. Understanding file I/O is a
    fundamental skill — let your brain do the work.
"""

import json
import os

# Path to the data directory — calculated relative to THIS file's location.
# os.path.dirname(__file__) gives us the folder containing storage.py,
# so this works regardless of where the user runs the program from.
# This is more robust than hardcoded "data/" which breaks if you
# run the script from a different working directory.
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def _ensure_data_dir():
    """
    Create the data/ directory if it doesn't exist.

    Called internally before any save operation. The leading underscore
    signals this is a private helper — not part of the public API.

    Why os.makedirs with exist_ok=True instead of checking os.path.exists:
        Avoids a race condition: between checking "does it exist?" and
        creating it, something else could create it, causing an error.
        exist_ok=True handles this safely.
    """
    # TODO: Implement this — it's one line!
    # Hint: os.makedirs(DATA_DIR, exist_ok=True)
    pass


def load_data(filename):
    """
    Load a JSON data file and return its contents.

    Parameters:
        filename (str): Name of the file (e.g., "books.json").
                        Will be loaded from the data/ directory.

    Returns:
        list[dict]: The parsed JSON data. Returns an empty list if the
        file doesn't exist yet (first run).

    Why return an empty list instead of raising an error:
        On first run, no data files exist. Treating "no file" as "no data"
        means the rest of the code doesn't need special first-run handling.
    """
    # TODO: Implement this function
    # Hints:
    #   - Build the full path: os.path.join(DATA_DIR, filename)
    #   - Use try/except for FileNotFoundError and json.JSONDecodeError
    #   - Return [] if the file doesn't exist or is corrupted
    pass


def save_data(filename, data):
    """
    Write data to a JSON file in the data/ directory.

    Parameters:
        filename (str): Name of the file (e.g., "books.json").
        data (list[dict]): The data to serialize.

    Returns:
        None

    Implementation notes:
        - Calls _ensure_data_dir() first (creates folder if needed)
        - Uses indent=2 for human-readable JSON (easy to debug)
        - Uses ensure_ascii=False so names with accents display correctly
    """
    # TODO: Implement this function
    # Hints:
    #   - Call _ensure_data_dir() first
    #   - Build the full path: os.path.join(DATA_DIR, filename)
    #   - Open with "w" mode and use json.dump(data, f, indent=2, ensure_ascii=False)
    pass


# ============================================================
# CONVENIENCE FUNCTIONS
# ============================================================
# One pair per entity type. These exist so the rest of the code
# reads load_books() / save_books() instead of
# load_data("books.json") / save_data("books.json", ...).
# It's a small readability win that prevents typos in filenames.
# ============================================================


def load_books():
    """Load all books from books.json."""
    return load_data("books.json")


def save_books(books):
    """Save the books list to books.json."""
    save_data("books.json", books)


def load_members():
    """Load all members from members.json."""
    return load_data("members.json")


def save_members(members):
    """Save the members list to members.json."""
    save_data("members.json", members)


def load_loans():
    """Load all loans from loans.json."""
    return load_data("loans.json")


def save_loans(loans):
    """Save the loans list to loans.json."""
    save_data("loans.json", loans)


# ============================================================
# TESTING THIS MODULE
# ============================================================
# Run this file directly to test save/load:
#   python storage.py
#
# It will save sample data, reload it, and verify the round trip.
# ============================================================

if __name__ == "__main__":
    # Quick self-test — run this file directly to verify save/load works
    print("Testing storage module...")

    test_books = [
        {"id": "B001", "title": "Clean Code", "author": "Robert Martin"},
        {"id": "B002", "title": "The Pragmatic Programmer", "author": "Hunt & Thomas"},
    ]

    save_books(test_books)
    loaded = load_books()

    if loaded == test_books:
        print("  PASS: Save and load round trip works!")
    else:
        print("  FAIL: Loaded data doesn't match saved data.")
        print(f"  Saved:  {test_books}")
        print(f"  Loaded: {loaded}")

    # Check that the file exists and is readable
    filepath = os.path.join(DATA_DIR, "books.json")
    if os.path.exists(filepath):
        print(f"  PASS: File created at {filepath}")
    else:
        print(f"  FAIL: File not found at {filepath}")

    print("Done! If both tests passed, storage.py is ready.")
