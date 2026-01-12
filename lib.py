import sys
def display_books(book_ids, titles, authors, years):
    print("\n------ Library Book Records ------")
    for i in range(len(book_ids)):
        print(f"Book ID: {book_ids[i]}, Title: {titles[i]}, Author: {authors[i]}, Year: {years[i]}")
def total_books(book_ids):
    return len(book_ids)
def book_category(years):
    old = 0
    new = 0
    for y in years:
        if int(y) < 2020:
            old += 1
        else:
            new += 1
    return old, new
if __name__ == "__main__":
    script_name = sys.argv[0]
    if len(sys.argv) > 4:
        library_name = sys.argv[1]
        book_ids = sys.argv[2].split(",")
        titles = sys.argv[3].split(",")
        authors = sys.argv[4].split(",")
        years = sys.argv[5].split(",")
        print("User provided library data")
    else:
        library_name = "City Library"
        book_ids = ["B1", "B2", "B3"]
        titles = ["Python", "Java", "AI"]
        authors = ["Guido", "James", "Andrew"]
        years = ["2021", "2019", "2023"]
        print("No input given – using default data")
    total = total_books(book_ids)
    old_books, new_books = book_category(years)
    print("\n========== Library Book Record System ==========")
    print("Script Name:", script_name)
    print("Library Name:", library_name)
    print("Total Books:", total)
    display_books(book_ids, titles, authors, years)
    print("\nOld Books (before 2020):", old_books)
    print("New Books (2020 and after):", new_books)
