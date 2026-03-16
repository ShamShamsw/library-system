"""
models.py — Data model constructors for library entities
==========================================================

Each function creates a new entity as a dictionary. We use functions
instead of classes because:
    1. At this skill level, dicts are more familiar than classes
    2. Dicts serialize to JSON natively (no custom encoder needed)
    3. The functions enforce consistent structure — every book dict
       has the same keys, just like a database row has fixed columns

Trade-off: Classes would give us type hints, methods, and __repr__.
For this project size, dicts are simpler. See stretch goals for
the class-based refactor.

BUILD THIS MODULE SECOND (after storage.py).

If You Get Stuck:
    Use an AI assistant to ASK QUESTIONS — for example:
      "How do I generate a formatted ID string like 'B001' in Python?"
      "How do I get today's date as a string in Python?"
    DO NOT ask AI to write the solution. Building data models is a
    core skill you need to own.
"""

from datetime import date, timedelta
from storage import load_books, load_members, load_loans

# ============================================================
# ID GENERATION
# ============================================================
# IDs use a prefix + 3-digit number format: "B001", "M001", "L001"
# This makes it easy to see what type of entity an ID refers to.
#
# Strategy: find the highest existing ID number, add 1.
# If no entities exist, start at 001.
#
# Note: IDs are NEVER reused. If you delete B002 and add a new book,
# it becomes B004 (not B002). This is the same as database auto-increment.
# ============================================================


def _generate_id(prefix, existing_items):
    """
    Generate the next unique ID for an entity type.

    Parameters:
        prefix (str): "B" for books, "M" for members, "L" for loans.
        existing_items (list[dict]): Current items (to find the max ID).

    Returns:
        str: A new unique ID like "B001", "B002", etc.

    Example:
        >>> _generate_id("B", [{"id": "B001"}, {"id": "B003"}])
        "B004"     # max is 3, so next is 4
    """
    # TODO: Implement this function
    # Hints:
    #   - If the list is empty, return f"{prefix}001"
    #   - Otherwise, extract the numeric part of each ID:
    #     numbers = [int(item["id"][1:]) for item in existing_items]
    #   - Find the max and add 1
    #   - Format with zero-padding: f"{prefix}{next_num:03d}"
    pass


# ============================================================
# ENTITY CONSTRUCTORS
# ============================================================


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
        dict: A book record with keys: id, title, author, isbn, genre, total_copies.

    Design note on ISBN validation:
        Real ISBNs have a checksum and strict format. Validating this is
        interesting but tangential to this project's goals. We accept any
        string. This comment shows it's a conscious choice, not an oversight.

    Note on available copies:
        We do NOT store "available_copies" on the book. It's CALCULATED
        from loans (total_copies - active_loans). Storing it would create
        a risk of the count getting out of sync with reality.
        This principle is called "single source of truth."
    """
    # TODO: Implement this function
    # Hints:
    #   - Call _generate_id("B", load_books()) to get the next ID
    #   - Return a dictionary with all the fields
    #   - Example: {"id": "B001", "title": title, "author": author, ...}
    pass


def create_member(name, email):
    """
    Create a new library member record.

    Parameters:
        name (str): Member's full name.
        email (str): Member's email address.

    Returns:
        dict: A member record with keys: id, name, email, join_date.
              join_date is automatically set to today.
    """
    # TODO: Implement this function
    # Hints:
    #   - Call _generate_id("M", load_members())
    #   - Use date.today().isoformat() for the join date
    pass


def create_loan(book_id, member_id, loan_days=14):
    """
    Create a new loan record linking a book to a member.

    Parameters:
        book_id (str): ID of the book being checked out (e.g., "B001").
        member_id (str): ID of the member checking it out (e.g., "M001").
        loan_days (int): Days until the book is due. Defaults to 14.

    Returns:
        dict: A loan record with keys:
            id, book_id, member_id, checkout_date, due_date, return_date.

    Why return_date starts as None:
        A loan with return_date=None means the book is still out.
        When returned, we SET return_date to today's date string.
        This single field tells us both status (active vs returned)
        and when it was returned. No need for a separate "status" field.
    """
    # TODO: Implement this function
    # Hints:
    #   - Call _generate_id("L", load_loans())
    #   - checkout_date = date.today().isoformat()
    #   - due_date = (date.today() + timedelta(days=loan_days)).isoformat()
    #   - return_date = None  (book hasn't been returned yet)
    pass


# ============================================================
# TESTING THIS MODULE
# ============================================================

if __name__ == "__main__":
    # Quick self-test — make sure the constructors work
    print("Testing models module...")

    book = create_book("Clean Code", "Robert Martin", "978-0132350884", "Software", 3)
    print(f"  Book: {book}")

    member = create_member("Alice Johnson", "alice@example.com")
    print(f"  Member: {member}")

    if book and member:
        loan = create_loan(book["id"], member["id"])
        print(f"  Loan: {loan}")

    print("Done! Check that all fields are present and IDs are generated.")
