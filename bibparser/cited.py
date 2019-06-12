from typing import Iterable
from enum import Enum

class SourceTypes(Enum):
    BOOK = "book"
    WEBSITE = "website"
    JOURNAL_ARTICLE = "journal_article"

class Source(object):
    """docstring for Source"""

    def __init__(self, source_type):
        self.source_type = source_type

    # TODO make this an abstract method. Look into ways to extend fields from parent fields.
    # prevent the fields array from being edited
    # there may be a better way to do this
    # @classmethod
    # def fields(cls):
        

    def __eq__(self, other):
        try:
            fields_eq = True
            for field in self.fields:
                # probably a better way to do this, but I'm not sure how
                fields_eq = (fields_eq
                    and getattr(self, field) == getattr(other, field)
                )
            return (self.source_type == other.source_type) and fields_eq
        except AttributeError as e:
            return False
    

class Book(Source):
    _fields = [
        "author_last",
        "author_first",
        "title",
        "published_at",
        "published_by",
        "published_year"
    ]

    def __init__(self, author_last, author_first, title, published_at, published_by, published_year):
        super(Book, self).__init__(SourceTypes.BOOK)
        self.author_last = author_last
        self.author_first = author_first
        self.title = title
        self.published_at = published_at
        self.published_by = published_by
        self.published_year = published_year

    @property
    def fields(cls) -> Iterable[str]:
        return cls._fields

    def __str__(self):
        return "{}, {}: {}".format(
                self.author_last.upper(),
                self.author_first,
                self.title
            )

class JournalArticle(Source):
    """docstring for JournalArticle"""

    _fields = ["journal_name"]

    def __init__(self):
        super(JournalArticle, self).__init__(SourceTypes.JOURNAL_ARTICLE)

    @property
    def fields(cls) -> Iterable[str]:
        return cls._fields
    
    def __str__(self):
        return "{}".format(
                self.source_type
            )