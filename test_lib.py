from lib import display_books, total_books, book_category

def test_total_books():
    book_ids = ["B1", "B2", "B3"]
    assert total_books(book_ids) == 3

def test_book_category_old_and_new():
    years = ["2018", "2021", "2019", "2023"]
    old, new = book_category(years)
    assert old == 2
    assert new == 2

def test_book_category_all_new():
    years = ["2020", "2021", "2022"]
    old, new = book_category(years)
    assert old == 0
    assert new == 3

def test_book_category_all_old():
    years = ["2015", "2018", "2019"]
    old, new = book_category(years)
    assert old == 3
    assert new == 0
