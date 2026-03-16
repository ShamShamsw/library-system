# Beginner Project 06: Library Management System

**Time:** 2.5–4 hours  
**Difficulty:** Beginner+  
**Focus:** Multi-entity data modeling, relational thinking, multi-file architecture, and writing documentation that a new team member could follow without any help

---

## Why This Project?

Every previous beginner project dealt with **one type of data** — contacts, expenses, grades. Real software manages **multiple related entities**. A library has books, members, AND loans — and a loan connects a book to a member. Learning to model these relationships is the single most important step toward backend development, databases, and system design interviews.

This project is your bridge from "I can write Python scripts" to "I can design a small system."

---

## More Projects

You can access this project and more in this separate repository:

[student-interview-prep](https://github.com/ShamShamsw/student-interview-prep.git)

---

## The Importance of Comments

This project introduces **system-level documentation** — writing comments that explain how the pieces fit together, not just how one function works.

### New commenting skill: relationship documentation

```python
# ============================================================
# DATA MODEL RELATIONSHIPS
# ============================================================
#
#   Member (1) ──────< (many) Loan >────── (1) Book
#
#   In plain English:
#     - One member can have many active loans
#     - Each loan belongs to exactly one member and one book
#     - A book can only be on loan to one member at a time
#
#   This is a classic "many-to-many through a join entity" pattern.
#   In a database, the Loan table acts as a junction/bridge table
#   between Members and Books. Here we model it with dictionaries
#   and use IDs to link them, exactly how a relational database works.
#
#   Why IDs instead of nested objects:
#     If we stored the full member dict inside each loan dict, we'd
#     have duplicated data. Change a member's name and you'd need to
#     update it in every loan. IDs avoid this — look up the current
#     member data by ID when you need it. This is "normalization" in
#     database terms.
# ============================================================
```

### New commenting skill: module-level architecture map

```python
# ============================================================
# FILE ARCHITECTURE
# ============================================================
#
#   library/
#   ├── main.py          ← Entry point: menu loop, user interaction
#   ├── models.py        ← Data creation: create_book(), create_member(), etc.
#   ├── storage.py       ← Persistence: load/save JSON data files
#   ├── operations.py    ← Business logic: checkout, return, search, overdue
#   ├── display.py       ← Formatting: tables, reports, summaries
#   └── data/
#       ├── books.json
#       ├── members.json
#       └── loans.json
#
#   Data flows one direction: main.py → operations.py → storage.py
#   Display is called from main.py but never modifies data.
#   This separation means you can change how data is stored (switch
#   from JSON to SQLite) without touching the display or business logic.
# ============================================================
```

---

## Requirements

Build a command-line library management system that supports:

### Books
1. **Add** a book (title, author, ISBN, genre, total copies)
2. **Search** books (by title, author, or genre — partial matches)
3. **List** all books (with availability status)
4. **Remove** a book (only if no copies are currently on loan)

### Members
1. **Register** a new member (name, email, membership date)
2. **Search** members (by name or email)
3. **List** all members
4. **View** a member's profile (personal info + current loans + loan history)

### Loans (the relationship between books and members)
1. **Check out** a book to a member (set a due date 14 days from today)
2. **Return** a book
3. **View** all current loans
4. **View** overdue books (due date has passed)

### Rules to enforce
- A member can have at most **3 books** checked out simultaneously
- A book can't be checked out if **all copies** are on loan
- A book can't be removed if **any copy** is currently on loan
- Returning a book that isn't checked out should show an error

### Example session:

```
╔══════════════════════════════════════════════════════╗
║              LIBRARY MANAGEMENT SYSTEM               ║
║              Books: 12 | Members: 5 | Loans: 3      ║
╚══════════════════════════════════════════════════════╝

Main Menu:
  1) Books
  2) Members
  3) Loans
  4) Reports
  5) Quit

Choice: 1

── Books ──────────────────────────────────────────────
  1) Add a book
  2) Search books
  3) List all books
  4) Remove a book
  5) Back to main menu

Choice: 3

┌──────┬──────────────────────────────┬────────────────────┬───────────┬───────────────┐
│ ID   │ Title                        │ Author             │ Genre     │ Availability  │
├──────┼──────────────────────────────┼────────────────────┼───────────┼───────────────┤
│ B001 │ Clean Code                   │ Robert Martin      │ Software  │ 2/3 available │
│ B002 │ The Pragmatic Programmer     │ Hunt & Thomas      │ Software  │ 1/1 available │
│ B003 │ Cracking the Coding Intervie │ Gayle McDowell     │ Interview │ 0/2 available │
│ B004 │ Introduction to Algorithms   │ Cormen et al.      │ CS        │ 1/1 available │
└──────┴──────────────────────────────┴────────────────────┴───────────┴───────────────┘
12 books total | 9 copies available | 3 copies on loan

Choice: 5

Choice: 3

── Loans ──────────────────────────────────────────────
  1) Check out a book
  2) Return a book
  3) View current loans
  4) View overdue books
  5) Back to main menu

Choice: 1
Member (name or ID): Alice
Book (title or ID): Clean Code

✓ Checked out "Clean Code" to Alice
  Due date: 2026-03-13 (14 days)
  Alice now has 2 of 3 allowed books

Choice: 3

Current loans (3):
┌──────┬──────────────────────────────┬──────────────┬────────────┬───────────┐
│ Loan │ Book                         │ Member       │ Due Date   │ Status    │
├──────┼──────────────────────────────┼──────────────┼────────────┼───────────┤
│ L001 │ Cracking the Coding Intervie │ Bob          │ 2026-02-20 │ ⚠ OVERDUE │
│ L002 │ Cracking the Coding Intervie │ Charlie      │ 2026-03-05 │ 6 days    │
│ L003 │ Clean Code                   │ Alice        │ 2026-03-13 │ 14 days   │
└──────┴──────────────────────────────┴──────────────┴────────────┴───────────┘

Choice: 5

Choice: 4

── Reports ────────────────────────────────────────────
  1) Overdue books
  2) Most popular books (by total checkouts)
  3) Most active members
  4) Library summary
  5) Back to main menu

Choice: 4

=== Library Summary ===
Total books:       12 titles (18 copies)
Total members:      5
Active loans:       3
Overdue loans:      1

Genre breakdown:
  Software:    5 titles  ██████████████████████████████████████░░ 42%
  Interview:   3 titles  ██████████████████████░░░░░░░░░░░░░░░░░ 25%
  CS:          2 titles  ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░ 17%
  Fiction:     2 titles  ██████████████░░░░░░░░░░░░░░░░░░░░░░░░░ 17%
```

---

## STOP — Plan Before You Code

Spend **25–35 minutes** planning. This is the most complex beginner project — thorough planning is essential.

### Planning Question 1: Data Models

Design the dictionary structure for each entity. Write these as comments FIRST.

**Book:**
```
What fields does a book need?
- id (str): Unique identifier like "B001" — why string, not int?
- title (str)
- author (str)
- isbn (str): Should this be validated? (For now, no — comment why)
- genre (str): Free text or from a predefined list?
- total_copies (int): How many the library owns
- (Do NOT store "available copies" — calculate it from loans. Why?
   Because stored counts can get out of sync. If you track both
   total_copies AND available_copies, a bug in checkout/return
   could make them inconsistent. Calculating from loans is the
   single source of truth.)
```

**Member:**
```
- id (str): "M001"
- name (str)
- email (str)
- join_date (str): Date in "YYYY-MM-DD" format
- (Loan history is NOT stored in the member — it's in the loans data.
   Why? Same reason: single source of truth. Query loans to find
   a member's history rather than duplicating data.)
```

**Loan:**
```
- id (str): "L001"
- book_id (str): Links to a book
- member_id (str): Links to a member
- checkout_date (str)
- due_date (str)
- return_date (str or null): null if still active, date string if returned
- (Why store returned loans instead of deleting them? History.
   You can show "Bob has checked out 15 books this year" only
   if you keep the records.)
```

### Planning Question 2: File Architecture

This project uses **multiple files**. Plan which functions go in which file:

- `main.py` — menu loops and user input (NO business logic here)
- `models.py` — `create_book()`, `create_member()`, `create_loan()` — functions that build data dictionaries
- `storage.py` — `load_books()`, `save_books()`, `load_members()`, etc.
- `operations.py` — `checkout_book()`, `return_book()`, `search_books()`, `get_overdue()`, `get_available_copies()`
- `display.py` — `format_books_table()`, `format_loans_table()`, `format_member_profile()`, etc.

**Why separate files?** Write a comment explaining each module's responsibility. The key principle: **each file has one reason to change.**
- If you redesign the menu → only `main.py` changes
- If you switch from JSON to SQLite → only `storage.py` changes
- If you change how tables look → only `display.py` changes

### Planning Question 3: ID Generation

You need unique IDs for books, members, and loans. Plan your strategy:
- Option A: Find the highest existing ID, add 1 → "B001", "B002", etc.
- Option B: Use a counter stored in the JSON file
- Option C: UUID
- **Which do you choose? Why?** (Hint: Option A has a subtle bug — what happens if you delete B002 and then add a new book? Does B002 get reused? Is that okay?)

### Planning Question 4: The "Available Copies" Calculation

This is the trickiest logic in the project. Plan it carefully:
```
available_copies = book.total_copies - (number of ACTIVE loans for this book)
An active loan is one where return_date is null.
```
- Which function computes this? Where does it live?
- Does it need all loans, or just loans for one book?
- Should it be called `get_available_copies(book_id, loans)` or should it be a property of the book somehow?

### Planning Question 5: Overdue Detection

```
A loan is overdue if:
  - return_date is null (still active)  AND
  - due_date < today's date
```
- How do you compare dates? (`datetime.strptime` to parse strings, then compare with `<`)
- Where does this logic live? (probably `operations.py`)
- How do you display it? ("⚠ OVERDUE" vs. "6 days left")

### Planning Question 6: Build Order

Plan the order you'll build and test each piece. A suggested order:
1. `storage.py` — save and load empty JSON files (test immediately)
2. `models.py` — create book and member dicts (test with print)
3. `operations.py` — add a book, add a member (test: add → save → reload → verify)
4. `display.py` — format a books table (test with hardcoded data)
5. `main.py` — books menu (integrate: add + list books through the menu)
6. `operations.py` — checkout and return logic (the hard part)
7. `main.py` — loans menu
8. `operations.py` — overdue and reports

**Stop and test after every step.** Don't build the whole thing and hope it works.

---

## Step-by-Step Instructions

### Step 1: Create the project structure and write your plan (25–35 minutes)

Create these files:

```
06-library-system/
├── main.py
├── models.py
├── storage.py
├── operations.py
├── display.py
└── data/          ← this folder will hold the JSON files
```

In **every file**, start with:
1. A module-level docstring explaining the file's purpose
2. A comment block showing where this file fits in the architecture
3. Function stubs with complete docstrings (no implementations yet)

In `main.py`, also include:
- The relationship diagram (see the comment example at the top of this README)
- The file architecture map
- Your planning block (40+ lines) answering all 6 planning questions

**At this point you should have 5 files with 150+ lines of comments total and zero working code. That IS the plan.**

### Step 2: Build the storage layer (15 minutes)

```python
# storage.py
"""
storage.py — Data persistence layer for the Library Management System.

Responsible for reading and writing JSON data files. No other module
should touch the filesystem directly — all data access goes through
this module.

Why JSON and not a database:
    For a project this size, JSON files are simpler to debug (you can
    open them in any text editor), require no additional dependencies,
    and teach the same persistence concepts. In a real library system,
    you'd use a relational database — see the stretch goals.

File locations:
    All data files live in the data/ subdirectory, relative to this
    script. Using a subdirectory keeps data separate from code.
"""

import json
import os

# Path to the data directory — calculated relative to THIS file's location.
# os.path.dirname(__file__) gives us the directory containing storage.py,
# so this works regardless of where the user runs the program from.
# This is more robust than a hardcoded "data/" which breaks if you
# run the script from a different working directory.
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def _ensure_data_dir():
    """
    Create the data/ directory if it doesn't exist.

    Called internally before any save operation. The leading underscore
    signals this is a private helper — not part of the public API.

    Why os.makedirs with exist_ok=True instead of checking os.path.exists:
        Race condition: between checking "does it exist?" and creating it,
        another process could create it, causing an error. exist_ok=True
        handles this atomically. In practice this rarely matters for a
        single-user CLI app, but it's a good habit that interviewers notice.
    """
    os.makedirs(DATA_DIR, exist_ok=True)


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
    # TODO: implement
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
        - Uses indent=2 for human-readable JSON (easy to debug)
        - Uses ensure_ascii=False so names with accents display correctly
    """
    # TODO: implement
    pass


# Convenience functions — one per entity type.
# These exist so the rest of the code reads load_books() / save_books()
# instead of load_data("books.json") / save_data("books.json", ...).
# It's a small readability win that prevents typos in filename strings.

def load_books():
    """Load all books from books.json."""
    return load_data("books.json")

def save_books(books):
    """Save the books list to books.json."""
    save_data("books.json", books)

# TODO: Add load_members, save_members, load_loans, save_loans
```

**Test immediately:** Save a hardcoded list of books, then load it back and print. Verify the JSON file appears in `data/`.

### Step 3: Build the models layer (10 minutes)

```python
# models.py
"""
models.py — Data model constructors for library entities.

Each function creates a new entity as a dictionary. We use functions
instead of classes because:
    1. At this skill level, dicts are more familiar than classes
    2. Dicts serialize to JSON natively (no custom encoder needed)
    3. The functions enforce consistent structure — every book dict
       has the same keys, just like a database row has fixed columns

Trade-off: Classes would give us type hints, methods, and __repr__.
For this project size, dicts are simpler. See stretch goals for the
class-based refactor.
"""

from datetime import date, timedelta


def create_book(title, author, isbn, genre, total_copies=1):
    """
    Create a new book record.

    Parameters:
        title (str): Book title.
        author (str): Author name(s).
        isbn (str): ISBN identifier (not validated — see design note).
        genre (str): Genre category.
        total_copies (int): Number of copies the library owns. Defaults to 1.

    Returns:
        dict: A book record with a generated ID.

    Design note on ISBN validation:
        Real ISBNs have a checksum digit and strict format (ISBN-10 or
        ISBN-13). Validating this is interesting but tangential to the
        project's learning goals. We accept any string. A comment here
        is better than silent acceptance — future you (or a teammate)
        can see this was a conscious choice, not an oversight.
    """
    # TODO: implement — generate ID, return dict
    pass


def create_member(name, email):
    """
    Create a new library member record.

    Parameters:
        name (str): Member's full name.
        email (str): Member's email address.

    Returns:
        dict: A member record with a generated ID and today's join date.
    """
    # TODO: implement
    pass


def create_loan(book_id, member_id, loan_days=14):
    """
    Create a new loan record linking a book to a member.

    Parameters:
        book_id (str): ID of the book being checked out.
        member_id (str): ID of the member checking out the book.
        loan_days (int): Number of days until the book is due. Defaults to 14.

    Returns:
        dict: A loan record with checkout date, due date, and null return date.

    Why return_date starts as None:
        A loan with return_date=None means the book is still out.
        When the book is returned, we SET return_date to today's date.
        This single field tells us both the loan status (active vs returned)
        and when it was returned. No need for a separate "status" field.
    """
    # TODO: implement
    pass
```

**Test:** Create a book, a member, and a loan. Print them. Verify all fields are present.

### Step 4: Build the operations layer — books and members (15 minutes)

```python
# operations.py (partial)
"""
operations.py — Business logic for the Library Management System.

This module contains all the rules and logic. It:
    - Calls storage.py to read/write data
    - Calls models.py to create new entities
    - Enforces rules (max 3 loans, can't remove loaned books, etc.)
    - NEVER prints anything — it returns results for display.py to format

Why "never prints":
    Separating logic from output makes functions testable. You can call
    checkout_book() in a test and check the return value without capturing
    stdout. It also means you could build a web UI later that calls the
    same operations — the logic doesn't assume a terminal.
"""

def add_book(title, author, isbn, genre, total_copies=1):
    """
    Add a new book to the library.

    Returns:
        dict: The newly created book record.
    """
    # TODO: implement — call create_book(), append to list, save
    pass


def search_books(query):
    """
    Search books by title, author, or genre (case-insensitive partial match).

    Parameters:
        query (str): The search term.

    Returns:
        list[dict]: Books where title, author, OR genre contains the query.

    Why case-insensitive partial match:
        Users don't remember exact titles. Searching "clean" should find
        "Clean Code". Using str.lower() on both the query and each field
        makes comparison case-insensitive. Using `in` gives partial match.

    Algorithm:
        For each book, check if query.lower() appears in any of:
        title.lower(), author.lower(), genre.lower().
        This is O(n * m) where n = number of books and m = average
        string length. For a library of < 10,000 books, this is instant.
        A real system would use a search index (like Elasticsearch).
    """
    # TODO: implement
    pass


def get_available_copies(book_id):
    """
    Calculate how many copies of a book are currently available.

    Parameters:
        book_id (str): The book's unique ID.

    Returns:
        int: Number of copies not currently on loan.

    Calculation:
        available = total_copies - active_loans_for_this_book
        An active loan is one where return_date is None.

    Why we calculate instead of storing:
        If we stored available_copies on the book, we'd need to update
        it on every checkout AND every return. If a bug skipped one
        update, the count would be wrong forever. By calculating from
        loans, the number is always correct — it's derived, not stored.
        This principle is called "single source of truth."
    """
    # TODO: implement
    pass
```

**Test:** Add 3 books, search for one, verify `get_available_copies` returns `total_copies` (no loans yet).

### Step 5: Build the operations layer — checkout and return (20 minutes)

This is the most complex step. Code carefully and comment heavily.

```python
def checkout_book(book_id, member_id):
    """
    Check out a book to a member.

    Parameters:
        book_id (str): ID of the book.
        member_id (str): ID of the member.

    Returns:
        dict: {"success": True, "loan": loan_dict, "message": "..."} on success.
        dict: {"success": False, "message": "..."} on failure.

    Why return a dict instead of raising exceptions:
        For expected failures (book unavailable, member at limit), a return
        value is cleaner than exceptions. Exceptions are for unexpected
        errors (file corruption, missing data). The distinction:
            - "No copies available" = expected, return {"success": False}
            - "books.json is corrupted" = unexpected, let it raise

    Business rules enforced:
        1. Book must exist
        2. Member must exist
        3. Book must have available copies (total - active loans > 0)
        4. Member must have fewer than 3 active loans

    Each rule check is a separate if-block with a comment explaining
    the rule. This makes it easy to add or modify rules later.
    """
    # TODO: implement — check all 4 rules, then create loan and save
    pass


def return_book(loan_id):
    """
    Process a book return by setting the loan's return_date to today.

    Parameters:
        loan_id (str): ID of the loan to close.

    Returns:
        dict: {"success": True, "message": "..."} on success.
        dict: {"success": False, "message": "..."} on failure.

    Why we set return_date instead of deleting the loan:
        Keeping returned loans gives us history — "How many books has
        Bob checked out this year?" requires historical records. We
        distinguish active from returned loans by checking return_date:
            active:   return_date is None
            returned: return_date is a date string
    """
    # TODO: implement
    pass


def get_overdue_loans():
    """
    Find all loans that are past their due date and not yet returned.

    Returns:
        list[dict]: Active loans where due_date < today, enriched with
        book title and member name for display purposes.

    Why "enriched" — adding book/member info to loan dicts:
        The loan dict only stores book_id and member_id. For display,
        we need the actual names. This function looks up each ID and
        adds "book_title" and "member_name" keys to each result.

        This is the Python equivalent of a SQL JOIN:
            SELECT loans.*, books.title, members.name
            FROM loans
            JOIN books ON loans.book_id = books.id
            JOIN members ON loans.member_id = members.id
            WHERE loans.return_date IS NULL AND loans.due_date < TODAY
    """
    # TODO: implement
    pass
```

**Test this extensively:**
- Check out a book → verify loan is created and availability drops by 1
- Return the book → verify return_date is set and availability goes back up
- Try to check out when no copies available → verify error message
- Try a 4th checkout for one member → verify the limit is enforced
- Create a loan with a past due date → verify `get_overdue_loans` finds it

### Step 6: Build the display layer (20 minutes)

```python
# display.py
"""
display.py — Output formatting for the Library Management System.

All print formatting lives here. Functions accept data and return
formatted strings. They do NOT call print() themselves (usually) —
the caller in main.py decides when to print.

Why separate display from logic:
    1. Testability: compare strings in tests without capturing stdout
    2. Flexibility: same data could be formatted as text, HTML, or PDF
    3. Single responsibility: changing a column width doesn't risk
       breaking checkout logic
"""

def format_books_table(books, loans):
    """
    Format a list of books as a bordered table with availability.

    Parameters:
        books (list[dict]): Book records.
        loans (list[dict]): All loans (needed to calculate availability).

    Returns:
        str: A formatted table string ready to print.

    Why this function needs loans:
        Availability (e.g., "2/3 available") is calculated from loans,
        not stored on the book. So the display function needs access
        to loans to show accurate numbers. An alternative design would
        have operations.py pre-calculate availability, but that adds
        a processing step every time we list books. Since we're already
        loading loans anyway, passing them here is simpler.
    """
    # TODO: implement with box-drawing characters
    pass


def format_member_profile(member, loans, books):
    """
    Format a detailed member profile showing current loans and history.

    Parameters:
        member (dict): The member record.
        loans (list[dict]): All loans (will be filtered to this member).
        books (list[dict]): All books (for title lookups).

    Returns:
        str: A formatted profile string.

    Sections:
        1. Member info (name, email, join date)
        2. Current loans (active, with due dates and overdue warnings)
        3. Loan history (returned books, with checkout/return dates)
        4. Statistics (total books borrowed, currently active, overdue count)
    """
    # TODO: implement
    pass
```

### Step 7: Build main.py — menus and integration (20 minutes)

```python
# main.py
"""
main.py — Entry point for the Library Management System.

This module handles all user interaction: displaying menus, reading
input, and routing to the appropriate operations. It follows the
"thin controller" pattern — minimal logic here, mostly delegation.

Architecture:
    User input → main.py → operations.py → storage.py → JSON files
    Display   ← main.py ← display.py

    main.py is the only module that uses input() or print().
    Every other module is "pure" (no I/O side effects), which
    makes the system testable and maintainable.
"""

from operations import (
    add_book, search_books, checkout_book,
    return_book, get_overdue_loans
)
from display import format_books_table, format_member_profile
from storage import load_books, load_members, load_loans


def main_menu():
    """
    Display the top-level menu and route user choices.

    Loop structure:
        while True → show menu → get choice → call sub-menu → repeat
        Only "Quit" breaks the loop.

    Why nested menu functions instead of one giant menu:
        A single function with 15+ options is hard to read and modify.
        Sub-menus (books_menu, members_menu, loans_menu) keep each
        function focused on one entity. Adding a new book operation
        means editing only books_menu().
    """
    # TODO: implement
    pass


def books_menu():
    """Handle the Books sub-menu: add, search, list, remove."""
    # TODO: implement
    pass


def members_menu():
    """Handle the Members sub-menu: register, search, list, view profile."""
    # TODO: implement
    pass


def loans_menu():
    """Handle the Loans sub-menu: checkout, return, view, overdue."""
    # TODO: implement
    pass


def reports_menu():
    """Handle the Reports sub-menu: overdue, popular, active members, summary."""
    # TODO: implement
    pass


if __name__ == "__main__":
    # Guard: only run the menu when this file is executed directly.
    # If someone imports main.py (e.g., for testing), the menu won't auto-start.
    main_menu()
```

### Step 8: Test everything end-to-end (15 minutes)

Run through this full test scenario:
1. Start fresh (no data files) → verify the system starts cleanly
2. Add 4 books (2 with multiple copies) → verify the table shows them
3. Register 3 members → verify the member list
4. Check out books to test the rules:
   - Check out 3 books to one member → all succeed
   - Try a 4th → verify the limit error
   - Check out all copies of a multi-copy book → verify "no copies available" error
5. Return a book → verify availability updates
6. Search for a book by partial title → verify results
7. View a member profile → verify loan history
8. Create an overdue loan (manually edit the JSON to set a past due date) → verify overdue report
9. Try to remove a book that has active loans → verify the error
10. Quit and restart → verify all data persists

---

## Comment Checklist

- [ ] Module-level docstring in ALL 5 files explaining the file's purpose (5+ lines each)
- [ ] Relationship diagram showing how books, members, and loans connect
- [ ] File architecture map showing the module dependency flow
- [ ] Planning block in main.py covering all 6 planning questions (40+ lines)
- [ ] Every function has a complete docstring with Parameters and Returns
- [ ] At least 5 functions document a "Why" design decision
- [ ] Business rules in `checkout_book` each have a comment explaining the rule
- [ ] The "single source of truth" principle is documented (calculated availability, loan history)
- [ ] ID generation strategy is explained with alternatives considered
- [ ] The `_ensure_data_dir` leading underscore convention is explained
- [ ] `if __name__ == "__main__"` guard present with comment in main.py
- [ ] Total comments across all files: 200+ lines

---

## Reflect on What You Learned

After finishing, write 2–3 sentences for EACH audience below. This is the capstone — you're describing a multi-file system with relational data. The ability to explain this clearly at every level is what separates junior developers from mid-level ones.

### To a friend (casual, no jargon)

> _"I built a thing that..."_
>
> Example: "I made a library system where you can add books, sign up members, and check books in and out. It tracks who has what, when it's due, and yells at you if a book is overdue. Everything saves to files so it remembers between sessions."

### To an employer (focus on skills and process)

> _"In this project I practiced..."_
>
> Example: "I designed and built a multi-file application with separated concerns — data models, storage, business logic, and display each in their own module. I modeled relationships between entities using ID references (the same pattern as foreign keys in a database) and enforced business rules like loan limits and availability checks."

### To a professor (technical, precise)

> _"This project demonstrates..."_
>
> Example: "This project demonstrates multi-entity data modeling with referential integrity enforced at the application layer, the repository pattern for JSON-backed persistence, separation of concerns across five modules following the single-responsibility principle, and derived state computation (availability calculated from loan records rather than stored, ensuring a single source of truth). I documented the data model relationships using an ER-style diagram in comments and justified architectural decisions including ID generation strategy and the choice of dictionaries over classes."

**Write yours in a comment block at the bottom of `main.py`:**
```python
# ============================================================
# WHAT I LEARNED
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
```

---

## Stretch Goals

1. **Refactor to classes:** Replace dicts with `Book`, `Member`, and `Loan` classes (comment: what are the trade-offs vs. dictionaries?)
2. **Switch to SQLite:** Replace JSON storage with a SQLite database (comment: how does this change the storage layer without affecting operations?)
3. **Add due-date reminders:** Show "due tomorrow" and "due in 3 days" warnings (comment: where should this check happen — on startup, or continuously?)
4. **Add a fine system:** Charge $0.50/day for overdue books (comment: should fines be stored or calculated? Apply the "single source of truth" lesson)
5. **Add unit tests:** Write pytest tests for `operations.py` that don't depend on file I/O (comment: how do you test without real JSON files? Hint: dependency injection or mock)
6. **Import/export:** Bulk-add books from a CSV file (comment: reuse the CSV skills from the Grade Report project)
