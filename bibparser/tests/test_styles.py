# pytest tests for the style classes
# run from the bibparser parent dir with
# python37 -m pytest
#  --- or ---
# pythonw -m pytest
# 

import pytest
from ..styles import chicago
from ..cited import Book

@pytest.fixture
def book():
    author_last = "author_last"
    author_first = "author_first"
    title = "title"
    published_at = "published_at"
    published_by = "published_by"
    published_year = "published_year"
    return Book(author_last, author_first, title, published_at, published_by, published_year)

def test_generate_book_citation(book):
    expected_citation = (
        book.author_last + ", " + book.author_first
        + "." + " "
        + book.title
        + "." + " "
        + book.published_at + ": " + book.published_by + ", " + book.published_year
        + "."
        )
    assert expected_citation == chicago.generate_book_citation(book)
