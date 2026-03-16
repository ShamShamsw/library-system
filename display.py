"""
display.py — Output formatting for the Library Management System
==================================================================

All print formatting lives here. Functions accept data and return
formatted strings. They generally do NOT call print() themselves —
the caller in main.py decides when to print.

Why separate display from logic:
    1. Testability: compare strings in tests without capturing stdout
    2. Flexibility: same data could be formatted as text, HTML, or PDF
    3. Single responsibility: changing a column width doesn't risk
       breaking checkout logic

BUILD THIS MODULE FOURTH (after storage, models, and operations).

If You Get Stuck:
    Use an AI assistant to ASK QUESTIONS — for example:
      "How do I left-align text in a Python f-string?"
      "How do box-drawing characters work in Python strings?"
    DO NOT ask AI to write the whole function. Formatting is tedious
    but learning f-string alignment is a skill you'll use forever.
"""

from datetime import date

# ============================================================
# TABLE FORMATTING HELPERS
# ============================================================


def _truncate(text, width):
    """
    Truncate text to fit within a given width.

    Parameters:
        text (str): The string to truncate.
        width (int): Maximum character width.

    Returns:
        str: Original text if it fits, or text[:width-1] + "…" if too long.

    Why truncate instead of wrapping:
        Tables need fixed column widths to align properly. Wrapping
        would break the alignment. Truncation with an ellipsis shows
        the user that text was cut off.
    """
    # TODO: Implement this — about 3 lines
    # Hint: if len(text) <= width: return text
    #       return text[:width - 1] + "…"
    pass


# ============================================================
# BOOK DISPLAY
# ============================================================


def format_books_table(books, loans):
    """
    Format a list of books as a bordered table with availability.

    Parameters:
        books (list[dict]): Book records.
        loans (list[dict]): All loans (needed to calculate availability).

    Returns:
        str: A formatted table string ready to print.

    Columns: ID | Title | Author | Genre | Availability
    Availability shows "X/Y available" where X = total - active loans.

    Why this function needs loans:
        Available copies = total_copies - active loans for that book.
        It's calculated, not stored (single source of truth).
    """
    # TODO: Implement this function
    # Hints:
    #   - If no books, return "No books in the library."
    #   - Define column widths (e.g., ID: 6, Title: 30, Author: 20, Genre: 10, Avail: 15)
    #   - Build header row, separator, data rows, footer
    #   - For availability: count loans where book_id matches AND return_date is None
    #   - Use f-string alignment: f"{value:<width}" for left-align
    #   - You can use simple borders (|, -, +) or box-drawing characters
    #
    # Simple table example:
    #   | ID   | Title                   | Author          | Available |
    #   |------|-------------------------|-----------------|-----------|
    #   | B001 | Clean Code              | Robert Martin   | 2/3       |
    pass


def format_members_table(members):
    """
    Format a list of members as a table.

    Parameters:
        members (list[dict]): Member records.

    Returns:
        str: Formatted table string.

    Columns: ID | Name | Email | Joined
    """
    # TODO: Implement this
    pass


def format_loans_table(loans):
    """
    Format a list of loans as a table with status info.

    Parameters:
        loans (list[dict]): Loan records (should be enriched with
                            "book_title" and "member_name" from operations).

    Returns:
        str: Formatted table string.

    Columns: Loan ID | Book | Member | Due Date | Status
    Status shows either "OVERDUE" or "X days left" based on due date.
    """
    # TODO: Implement this
    # Hints:
    #   - For status, compare due_date to today:
    #     if due_date < date.today().isoformat(): status = "OVERDUE"
    #     else: calculate days remaining
    #   - To calculate days remaining:
    #     from datetime import datetime
    #     due = datetime.strptime(loan["due_date"], "%Y-%m-%d").date()
    #     days_left = (due - date.today()).days
    pass


def format_member_profile(member, loans, books):
    """
    Format a detailed member profile.

    Parameters:
        member (dict): The member record.
        loans (list[dict]): ALL loans (will filter to this member).
        books (list[dict]): ALL books (for title lookups).

    Returns:
        str: Multi-section profile string.

    Sections:
        1. Member info (name, email, join date)
        2. Current loans (active, with due dates and overdue warnings)
        3. Loan history (returned books, with dates)
        4. Stats (total borrowed, currently active, overdue count)
    """
    # TODO: Implement this
    # Hints:
    #   - Filter loans: member_loans = [l for l in loans if l["member_id"] == member["id"]]
    #   - Split into active (return_date is None) and returned
    #   - Look up book titles: create a dict {b["id"]: b["title"] for b in books}
    pass


def format_overdue_report(overdue_loans):
    """
    Format a report of overdue books.

    Parameters:
        overdue_loans (list[dict]): Overdue loan records (enriched).

    Returns:
        str: Formatted overdue report.
    """
    # TODO: Implement this
    # Show: book title, member name, due date, days overdue
    pass


def format_library_summary(summary):
    """
    Format the library summary with a genre bar chart.

    Parameters:
        summary (dict): Summary data from operations.get_library_summary().

    Returns:
        str: Formatted summary with stats and genre breakdown bar chart.

    Bar chart: same approach as the expense tracker —
        largest genre gets full bar, others are proportional.
    """
    # TODO: Implement this
    # Hints:
    #   - Display totals: books, copies, members, active loans, overdue
    #   - Genre breakdown as a bar chart using "█" and "░"
    #   - Max bar width = 20 characters
    pass


# ============================================================
# TESTING THIS MODULE
# ============================================================

if __name__ == "__main__":
    print("Testing display module...")
    print("(Uses sample data — doesn't need real JSON files)")
    print()

    # Test with sample data
    sample_books = [
        {
            "id": "B001",
            "title": "Clean Code",
            "author": "Robert Martin",
            "isbn": "978-0132350884",
            "genre": "Software",
            "total_copies": 3,
        },
        {
            "id": "B002",
            "title": "The Pragmatic Programmer",
            "author": "Hunt & Thomas",
            "isbn": "978-0135957059",
            "genre": "Software",
            "total_copies": 1,
        },
    ]

    sample_loans = [
        {
            "id": "L001",
            "book_id": "B001",
            "member_id": "M001",
            "checkout_date": "2026-02-15",
            "due_date": "2026-03-01",
            "return_date": None,
        },
    ]

    table = format_books_table(sample_books, sample_loans)
    if table:
        print(table)
    else:
        print("  format_books_table returned None — implement it!")

    print()
    print("Done!")
