
# book_search.py (Student A - Issue #1)

BOOKS = [
    {"title": "Software Engineering", "author": "Ian Sommerville"},
    {
        "title": "Software Engineering: A Practitioner's Approach",
        "author": "Roger Pressman"
    },
    {"title": "Clean Code", "author": "Robert C. Martin"},
]


def search_books(keyword, books=BOOKS):
    """Return books whose title or author contains the keyword."""
    if not keyword or not keyword.strip():
        raise ValueError("Keyword cannot be empty")

    k = keyword.strip().lower()

    return [
        book for book in books
        if k in book["title"].lower()
        or k in book["author"].lower()
    ]
