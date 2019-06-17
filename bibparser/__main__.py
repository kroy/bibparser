from styles import chicago
from cited import JournalArticle, Book

def call_me_by_my_name():
    # parse_func = chicago.parse
    # print(parse_func("bargive garble snook"))
    book1 = Book("author_last", "author_first", "title", "published_at", "published_by", "published_year")
    book2 = chicago.parse("boglle")
    print(book2 == book1)

call_me_by_my_name()