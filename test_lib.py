from lib import LibraryBook

def test_book_age_old():
    book = LibraryBook("B1", "Python", "Guido", 2018)
    assert book.book_age() == "Old Book"

def test_book_age_new():
    book = LibraryBook("B2", "AI", "Andrew", 2022)
    assert book.book_age() == "New Book"

def test_validate_book_valid():
    book = LibraryBook("B3", "Java", "James", 2021)
    assert book.validate_book() == "Valid Book"

def test_validate_book_invalid():
    book = LibraryBook("", "", "Unknown", 2020)
    assert book.validate_book() == "Invalid Book"
