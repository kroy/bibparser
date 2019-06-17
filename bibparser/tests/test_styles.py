# pytest tests for the style classes
# run from the bibparser parent dir with
# python37 -m pytest
#  --- or ---
# pythonw -m pytest
# 

import pytest
from styles import chicago
from cited import Book

@pytest.fixture
def book():
    return Book("author_last", "author_first", "title", "published_at", "published_by", "published_year")

def test_chicago_generate_book_citation(book):
    expected_citation = (
        book.author_last + ", " + book.author_first
        + "." + " "
        + book.title
        + "." + " "
        + book.published_at + ": " + book.published_by + ", " + book.published_year
        + "."
        )
    assert expected_citation == chicago.generate_book_citation(book)

def test_chicago_parse_with_book(book):
    # might not want to have styles.chicago both generate and parse the citation, but for now it's ok
    book_citation = chicago.generate_book_citation(book)
    parsed_source = chicago.parse(book_citation)
    assert parsed_source == book
