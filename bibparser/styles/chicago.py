from cited import Source, Book, JournalArticle

separator = "."

def parse(bib_entry: str) -> Source:
    # figure out what type of cited this entry represents
    # return the appropriate object
    # 
    return Book("author_last", "author_first", "title", "published_at", "published_by", "published_year")

# take a cited.Book object and turn it into a Chicago/Turabian style citation
def generate_book_citation(book: Book) -> str:
    return (
        book.author_last + ", " + book.author_first
        + separator + " "
        + book.title
        + separator + " "
        + book.published_at + ": " + book.published_by + ", " + book.published_year
        + separator
        )