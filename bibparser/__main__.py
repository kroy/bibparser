from styles import chicago
from cited import JournalArticle, Book

def call_me_by_my_name():
    # parse_func = chicago.parse
    # print(parse_func("bargive garble snook"))
    book1 = Book("roy", "kiron", "abd", "nyc", "butts", "1993")
    book2 = Book("roy", "kiron", "abd", "nyc", "butts", "1993")
    journ = JournalArticle()
    print(JournalArticle == book1)

call_me_by_my_name()