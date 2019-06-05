# pytest tests for the style classes
# run with pytest from the bibparser parent dir

from ..styles import chicago
from ..cited import Book

def test_generate_book_citation():
    author_last = "author_last"
    author_first = "author_first"
    title = "title"
    published_at = "published_at"
    published_by = "published_by"
    published_year = "published_year"
    book = Book(author_last, author_first, title, published_at, published_by, published_year)
    expected_citation = (
        author_last + ", " + author_first
        + "." + " "
        + title
        + "." + " "
        + published_at + ": " + published_by + ", " + published_year
        + "."
        )
    assert expected_citation == chicago.generate_book_citation(book)