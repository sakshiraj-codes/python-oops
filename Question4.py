""" Design a class Library that represents a library, which can have multiple books.
The Library class should have the following methods:
add_book(book): Add a book to the library.
remove_book(book): Remove a book from the library.
get_available_books(): Return a list of all available books in the library.
get_books_by_author(author): Return a list of books written by a specific author.
get_books_by_genre(genre): Return a list of books of a specific genre.
The Book class should have attributes like title, author, genre, etc."""

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library.")

    def get_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books

    def get_books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book.title)
        return books_by_author

    def get_books_by_genre(self, genre):
        books_by_genre = []
        for book in self.books:
            if book.genre == genre:
                books_by_genre.append(book.title)
        return books_by_genre

# Usage example:

# Create Book objects
book1 = Book("Book 1", "Author 1", "Genre 1")
book2 = Book("Book 2", "Author 2", "Genre 1")
book3 = Book("Book 3", "Author 1", "Genre 2")

# Create Library object
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Get available books in the library
print("Available books: ", library.get_available_books())  # Output: ['Book 1', 'Book 2', 'Book 3']

# Get books by author
print("Books by Author 1: ", library.get_books_by_author("Author 1"))  # Output: ['Book 1', 'Book 3']

# Get books by genre
print("Books in Genre 1: ", library.get_books_by_genre("Genre 1"))  # Output: ['Book 1', 'Book 2']