from cited import Book, JournalArticle

separator = "."

def parse(bib_entry):
    # figure out what type of cited this entry represents
    # return the appropriate object
    pass

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