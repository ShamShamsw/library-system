"""
main.py — Entry point for the Library Management System
=========================================================

This module handles all user interaction: displaying menus, reading
input, and routing to the appropriate operations. It follows the
"thin controller" pattern — minimal logic here, mostly delegation.

Architecture:
    User input → main.py → operations.py → storage.py → JSON files
    Display   ← main.py ← display.py

    main.py is the only module that uses input() or print().
    Every other module is "pure" (no I/O side effects), which
    makes the system testable and maintainable.

YOUR TASK: Fill in every function marked with TODO.
Read the README.md in this folder FIRST for the full instructions.

TIME ESTIMATE: 2.5–4 hours (for the ENTIRE project, not just this file)

IMPORTANT — If You Get Stuck:
    1. Re-read the README section for the step you're on.
    2. Build and test ONE module at a time, in this order:
       storage.py → models.py → operations.py → display.py → main.py
    3. Use an AI assistant (like Copilot Chat) to ASK QUESTIONS about
       concepts you don't understand — for example:
         "How do I import functions from another file in Python?"
         "How do I calculate the difference between two dates?"
         "What does 'foreign key' mean in plain English?"
       DO NOT ask AI to write the solution for you. The learning happens
       when YOUR brain figures out how to connect the pieces. AI is a
       tutor, not a shortcut. If AI writes your code, you skip the
       struggle that actually builds understanding.
    4. Python docs: https://docs.python.org/3/library/datetime.html

============================================================
DATA MODEL RELATIONSHIPS
============================================================

    Member (1) ──────< (many) Loan >────── (1) Book

    In plain English:
      - One member can have many active loans
      - Each loan belongs to exactly one member and one book
      - A book can only be checked out if it has available copies

    This is a classic "many-to-many through a join entity" pattern.
    In a database, the Loan table acts as a junction/bridge table
    between Members and Books. Here we model it with dictionaries
    and use IDs to link them — exactly how a relational database works.

    Why IDs instead of nested objects:
      If we stored the full member dict inside each loan dict, we'd
      have duplicated data. Change a member's name and you'd need to
      update it in every loan. IDs avoid this — look up the current
      member data by ID when you need it. This is "normalization."

============================================================
FILE ARCHITECTURE
============================================================

    06-library-system/
    ├── main.py          ← You are here. Menu loop, user interaction.
    ├── models.py        ← Data creation: create_book(), create_member(), etc.
    ├── storage.py       ← Persistence: load/save JSON data files.
    ├── operations.py    ← Business logic: checkout, return, search, overdue.
    ├── display.py       ← Formatting: tables, reports, summaries.
    └── data/            ← JSON data files (created automatically).
        ├── books.json
        ├── members.json
        └── loans.json

    Data flows one direction: main.py → operations.py → storage.py
    Display is called from main.py but never modifies data.

============================================================
PLANNING (fill in your answers below)
============================================================

    Build order:
        1. storage.py — save and load JSON files (test with hardcoded data)
        2. models.py — create_book, create_member, create_loan (test with print)
        3. operations.py — add_book, add_member (test: add → save → reload)
        4. display.py — format_books_table (test with hardcoded data)
        5. main.py — books menu (integrate: add + list books)
        6. operations.py — checkout and return (the hard part!)
        7. main.py — loans menu
        8. operations.py — overdue detection and reports

    Business rules:
        - Max 3 active loans per member
        - Can't check out a book with 0 available copies
        - Can't remove a book that has active loans
        - Return date = None means the loan is active

    ID generation strategy:
        - Format: "B001", "M001", "L001" (prefix + 3-digit number)
        - Find max existing ID, add 1
        - (What if you delete ID B002 then add a new book? It gets B004,
          not B002. IDs are never reused — like database auto-increment.)
"""

# TODO: Uncomment these imports once you've built the other modules
# from operations import (
#     add_book, search_books, list_all_books, remove_book,
#     register_member, search_members, list_all_members, view_member_profile,
#     checkout_book, return_book, list_current_loans, get_overdue_loans,
#     get_library_summary
# )
# from display import (
#     format_books_table, format_members_table, format_loans_table,
#     format_member_profile, format_overdue_report, format_library_summary
# )


def main_menu():
    """
    Display the top-level menu and route to sub-menus.

    Loop structure:
        while True → show menu → get choice → call sub-menu → repeat
        Only "Quit" breaks the loop.

    Why nested menu functions instead of one giant menu:
        A single function with 15+ options is hard to read. Sub-menus
        keep each function focused on one entity. Adding a new book
        operation means editing only books_menu().
    """
    # TODO: Implement the main menu loop
    # Hints:
    #   - Print a welcome banner with book/member/loan counts
    #   - Show options: 1) Books  2) Members  3) Loans  4) Reports  5) Quit
    #   - Route to the appropriate sub-menu function
    #   - Break out of the loop on "Quit"
    print("=" * 55)
    print("         LIBRARY MANAGEMENT SYSTEM")
    print("=" * 55)
    print()
    print("  [Start by building storage.py and models.py first!]")
    print("  [Then come back here to build the menus.]")
    print()
    pass


def books_menu():
    """
    Handle the Books sub-menu: add, search, list, remove.

    Options:
        1) Add a book — prompt for title, author, isbn, genre, copies
        2) Search books — prompt for search query
        3) List all books — show formatted table with availability
        4) Remove a book — by ID, only if no active loans
        5) Back to main menu
    """
    # TODO: Implement the books sub-menu
    # Hints:
    #   - Use a while True loop (break on "Back")
    #   - For "Add": collect inputs, call add_book()
    #   - For "Search": get query, call search_books(), display results
    #   - For "List": call list_all_books(), format with display module
    #   - For "Remove": get book ID, call remove_book(), show result
    pass


def members_menu():
    """
    Handle the Members sub-menu: register, search, list, view profile.

    Options:
        1) Register a new member — prompt for name and email
        2) Search members — by name or email
        3) List all members
        4) View member profile — show info + current loans + history
        5) Back to main menu
    """
    # TODO: Implement the members sub-menu
    pass


def loans_menu():
    """
    Handle the Loans sub-menu: checkout, return, view current, view overdue.

    Options:
        1) Check out a book — prompt for member and book (by name or ID)
        2) Return a book — prompt for loan ID
        3) View current loans — show all active loans
        4) View overdue books — show loans past due date
        5) Back to main menu
    """
    # TODO: Implement the loans sub-menu
    # This is the most complex menu — checkout needs to:
    #   1. Identify the member (by name or ID)
    #   2. Identify the book (by title or ID)
    #   3. Call checkout_book() which enforces all business rules
    #   4. Display the result (success or error message)
    pass


def reports_menu():
    """
    Handle the Reports sub-menu.

    Options:
        1) Overdue books report
        2) Most popular books (by total checkouts)
        3) Most active members (by total loans)
        4) Library summary (totals, genre breakdown)
        5) Back to main menu
    """
    # TODO: Implement the reports sub-menu
    pass


if __name__ == "__main__":
    # Guard: only run the menu when this file is executed directly.
    # If someone imports main.py (e.g., for testing), the menu won't auto-start.
    main_menu()


# ============================================================
# WHAT I LEARNED (fill this in AFTER you finish the entire project)
# ============================================================
# Friend:    ...
# Employer:  ...
# Professor: ...
# ============================================================
