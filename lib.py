class LibraryBook:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def book_age(self):
        if int(self.year) < 2020:
            return "Old Book"
        else:
            return "New Book"

    def validate_book(self):
        if not self.book_id or not self.title:
            return "Invalid Book"
        return "Valid Book"
