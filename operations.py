"""
operations.py — Business logic for the Library Management System
==================================================================

This module contains all the rules and logic. It:
    - Calls storage.py to read/write data
    - Calls models.py to create new entities
    - Enforces business rules (max 3 loans, can't remove loaned books, etc.)
    - NEVER prints anything — returns results for display.py to format

Why "never prints":
    Separating logic from output makes functions testable. You can call
    checkout_book() in a test and check the return value without capturing
    stdout. It also means you could build a web UI that calls the same
    operations — the logic doesn't assume a terminal.

BUILD THIS MODULE THIRD (after storage.py and models.py).

If You Get Stuck:
    Use an AI assistant to ASK QUESTIONS about logic — for example:
      "How do I count items in a list that match a condition in Python?"
      "How do I compare date strings in Python?"
    DO NOT ask AI to write the solution. Business logic is the heart of
    any application — this is where the real learning happens.
"""

from datetime import date
from storage import (
    load_books,
    save_books,
    load_members,
    save_members,
    load_loans,
    save_loans,
)
from models import create_book, create_member, create_loan

# ============================================================
# BOOK OPERATIONS
# ============================================================


def add_book(title, author, isbn, genre, total_copies=1):
    """
    Add a new book to the library.

    Parameters:
        title, author, isbn, genre (str): Book details.
        total_copies (int): Number of copies.

    Returns:
        dict: The newly created book record.
    """
    # TODO: Implement this
    # Steps: create_book() → load existing books → append → save → return
    pass


def search_books(query):
    """
    Search books by title, author, or genre (case-insensitive partial match).

    Parameters:
        query (str): The search term.

    Returns:
        list[dict]: Matching books.

    Algorithm:
        For each book, check if query.lower() appears in any of
        title.lower(), author.lower(), or genre.lower().
        This is O(n) where n = number of books.
    """
    # TODO: Implement this
    # Hint: [b for b in load_books() if query.lower() in b["title"].lower()
    #        or query.lower() in b["author"].lower()
    #        or query.lower() in b["genre"].lower()]
    pass


def list_all_books():
    """
    Get all books with their availability info.

    Returns:
        list[dict]: All books (use get_available_copies for each).
    """
    # TODO: Implement this — simply return load_books()
    pass


def remove_book(book_id):
    """
    Remove a book, but only if no copies are currently on loan.

    Parameters:
        book_id (str): The book's ID.

    Returns:
        dict: {"success": True/False, "message": "..."}

    Business rule: Can't delete a book with active loans. This prevents
    orphaned loan records that reference a non-existent book.
    """
    # TODO: Implement this
    # Steps:
    #   1. Find the book by ID
    #   2. Check if any active loans reference this book_id
    #   3. If active loans exist: return failure message
    #   4. If no active loans: remove from list, save, return success
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
        An active loan has return_date == None.

    Why calculate instead of store:
        If we stored available_copies, a bug in checkout/return could
        make it inconsistent with reality. Calculating from loans is
        always correct — "single source of truth."
    """
    # TODO: Implement this
    # Hints:
    #   - Find the book by ID to get total_copies
    #   - Count loans where book_id matches AND return_date is None
    #   - Return total_copies - active_loan_count
    pass


# ============================================================
# MEMBER OPERATIONS
# ============================================================


def register_member(name, email):
    """
    Register a new library member.

    Parameters:
        name (str): Member name.
        email (str): Member email.

    Returns:
        dict: The newly created member record.
    """
    # TODO: Implement this (same pattern as add_book)
    pass


def search_members(query):
    """
    Search members by name or email (case-insensitive partial match).

    Parameters:
        query (str): Search term.

    Returns:
        list[dict]: Matching members.
    """
    # TODO: Implement this
    pass


def list_all_members():
    """Get all members."""
    # TODO: return load_members()
    pass


def get_member_active_loans(member_id):
    """
    Get all active (unreturned) loans for a specific member.

    Parameters:
        member_id (str): The member's ID.

    Returns:
        list[dict]: Active loans for this member.
    """
    # TODO: Implement this
    # Hint: [l for l in load_loans() if l["member_id"] == member_id
    #        and l["return_date"] is None]
    pass


# ============================================================
# LOAN OPERATIONS (the complex part!)
# ============================================================


def checkout_book(book_id, member_id):
    """
    Check out a book to a member.

    Parameters:
        book_id (str): ID of the book.
        member_id (str): ID of the member.

    Returns:
        dict: {"success": True, "loan": loan_dict, "message": "..."} on success.
        dict: {"success": False, "message": "..."} on failure.

    Business rules enforced (check ALL of these):
        1. Book must exist
        2. Member must exist
        3. Book must have available copies (get_available_copies > 0)
        4. Member must have < 3 active loans

    Why return a dict instead of raising exceptions:
        "No copies available" is an expected situation, not a bug.
        Return values handle expected failures cleanly. Exceptions
        are for unexpected errors (corrupt file, missing data).
    """
    # TODO: Implement this function — this is the hardest part!
    # Steps:
    #   1. Load books and find the book by ID. If not found → failure.
    #   2. Load members and find the member by ID. If not found → failure.
    #   3. Check available copies with get_available_copies(book_id).
    #      If 0 → failure with message "No copies available."
    #   4. Check member's active loans with get_member_active_loans(member_id).
    #      If >= 3 → failure with message "Member has reached the 3-book limit."
    #   5. All checks passed! Create the loan with create_loan(book_id, member_id).
    #   6. Load loans, append the new loan, save loans.
    #   7. Return success with the loan data.
    pass


def return_book(loan_id):
    """
    Process a book return by setting the loan's return_date to today.

    Parameters:
        loan_id (str): ID of the loan to close.

    Returns:
        dict: {"success": True/False, "message": "..."}

    Why set return_date instead of deleting the loan:
        Keeping returned loans gives us loan history. You can answer
        "How many books has Bob borrowed this year?" only with history.
    """
    # TODO: Implement this
    # Steps:
    #   1. Load all loans
    #   2. Find the loan by ID
    #   3. If not found → failure
    #   4. If return_date is already set → failure ("already returned")
    #   5. Set return_date to date.today().isoformat()
    #   6. Save loans
    #   7. Return success
    pass


def list_current_loans():
    """
    Get all active (unreturned) loans, enriched with book/member names.

    Returns:
        list[dict]: Active loans with added "book_title" and "member_name".

    Why "enriched" — adding names to loan dicts:
        Loan dicts only store IDs. For display, we need actual names.
        This function looks up each ID and adds the info.

        This is the Python equivalent of a SQL JOIN:
            SELECT loans.*, books.title, members.name
            FROM loans JOIN books JOIN members ...
    """
    # TODO: Implement this
    # Hints:
    #   - Load books, members, and loans
    #   - Create lookup dicts: {b["id"]: b["title"] for b in books}
    #   - Filter loans where return_date is None
    #   - Add "book_title" and "member_name" to each loan
    pass


def get_overdue_loans():
    """
    Find all loans that are past their due date and not yet returned.

    Returns:
        list[dict]: Overdue loans, enriched with book/member names.

    A loan is overdue when:
        return_date is None  AND  due_date < today (as date strings)

    Date comparison note:
        Because dates are in "YYYY-MM-DD" format, string comparison
        works correctly: "2026-02-20" < "2026-02-27" is True.
        This is one reason we use ISO format for dates.
    """
    # TODO: Implement this
    # Hint: filter list_current_loans() where due_date < date.today().isoformat()
    pass


def get_library_summary():
    """
    Generate a summary of the library's current state.

    Returns:
        dict with keys:
            - "total_books": number of unique book titles
            - "total_copies": sum of all copies
            - "total_members": number of members
            - "active_loans": count of unreturned loans
            - "overdue_loans": count of overdue loans
            - "genre_breakdown": dict of {genre: count}
    """
    # TODO: Implement this
    pass


# ============================================================
# HELPER — Find entity by ID
# ============================================================


def _find_by_id(items, item_id):
    """
    Find a single item in a list by its "id" field.

    Parameters:
        items (list[dict]): List to search.
        item_id (str): The ID to find.

    Returns:
        dict or None: The matching item, or None if not found.

    Why a helper function:
        We look up items by ID in many places (checkout, return, remove,
        display). Writing this once avoids duplicating the search logic.
    """
    # TODO: Implement this — it's a simple loop
    # Hint: for item in items:
    #           if item["id"] == item_id:
    #               return item
    #       return None
    pass


# ============================================================
# TESTING THIS MODULE
# ============================================================

if __name__ == "__main__":
    print("Testing operations module...")
    print("(Make sure storage.py and models.py work first!)")
    print()

    # Test adding a book
    book = add_book("Test Book", "Test Author", "000-0000000000", "Test", 2)
    print(f"  Added book: {book}")

    # Test adding a member
    member = register_member("Test User", "test@example.com")
    print(f"  Registered member: {member}")

    # Test checkout
    if book and member:
        result = checkout_book(book["id"], member["id"])
        print(f"  Checkout result: {result}")

        # Test available copies
        available = get_available_copies(book["id"])
        print(f"  Available copies: {available} (should be 1)")

    print()
    print("Done! Check the data/ folder for the JSON files.")
