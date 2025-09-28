from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
        self._checked_out = False

    @abstractmethod
    def display_info(self):
        pass

    def check_out(self):
        if self._checked_out:
            print(f"'{self._title}' is already checked out.")
        else:
            self._checked_out = True
            print(f"'{self._title}' has been checked out.")

    def return_book(self):
        if not self._checked_out:
            print(f"'{self._title}' is not currently checked out.")
        else:
            self._checked_out = False
            print(f"'{self._title}' has been returned.")

    def is_checked_out(self):
        return self._checked_out

    def __eq__(self, other):
        if isinstance(other, Book):
            return self._title == other._title
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self._pages < other._pages
        return NotImplemented

class PrintedBook(Book):
    def __init__(self, title, author, pages, shelf_location):
        super().__init__(title, author, pages)
        self._shelf_location = shelf_location

    def display_info(self):
        status = "Checked Out" if self._checked_out else "Available"
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Pages: {self._pages}")
        print(f"Shelf Location: {self._shelf_location}")
        print(f"Status: {status}\n")

class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self._file_size_mb = file_size_mb

    def display_info(self):
        status = "Checked Out" if self._checked_out else "Available"
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Pages: {self._pages}")
        print(f"File Size: {self._file_size_mb} MB")
        print(f"Status: {status}\n")

if __name__ == "__main__":
    book1 = PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", 180, "A12")
    book2 = EBook("Python 101", "Mike Driscoll", 250, 1.5)
    book3 = PrintedBook("1984", "George Orwell", 328, "B03")
    book4 = EBook("Python 101", "Mike Driscoll", 250, 1.5)

    books = [book1, book2, book3, book4]

    books.sort()

    print("=== Book Info ===\n")
    for book in books:
        book.display_info()

    book1.check_out()
    book1.check_out()
    book1.return_book()
    book1.return_book()

    print()

    # Compare books
    print("=== Book Comparisons ===\n")
    print(f"'{book2._title}' == '{book4._title}':", book2 == book4)
    print(f"'{book1._title}' < '{book2._title}':", book1 < book2)
