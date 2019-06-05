from enum import Enum

class SourceTypes(Enum):
    BOOK = "book"
    WEBSITE = "website"
    JOURNAL_ARTICLE = "journal_article"

class Source(object):
    """docstring for Source"""
    def __init__(self, source_type):
        self.source_type = source_type

class Book(Source):
    def __init__(self, author_last, author_first, title, published_at, published_by, published_year):
        super(Book, self).__init__(SourceTypes.BOOK)
        self.author_last = author_last
        self.author_first = author_first
        self.title = title
        self.published_at = published_at
        self.published_by = published_by
        self.published_year = published_year

    def __str__(self):
        return "{}, {}: {}".format(
                self.author_last.upper(),
                self.author_first,
                self.title
            )

class JournalArticle(Source):
    """docstring for JournalArticle"""
    def __init__(self):
        super(JournalArticle, self).__init__(SourceTypes.JOURNAL_ARTICLE)
    
    def __str__(self):
        return "{}".format(
                self.source_type
            )