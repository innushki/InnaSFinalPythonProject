from shelf import Shelf
from reader import Reader
from book import Book

class Library:
    def __init__(self):
        self.shelves = []
        for i in range(3):
            self.shelves.append(Shelf())
        self.readers = []
        self.initializeShelves()

    def initializeShelves(self):
        book1 = Book("J.K. Rowling", "Harry Potter", 309)
        book2 = Book("George Orwell", "1984", 328)
        book3 = Book("J.R.R. Tolkien", "The Hobbit", 310)
        book4 = Book("Harper Lee", "To Kill a Mockingbird", 281)
        book5 = Book("Jane Austen", "Pride and Prejudice", 279)
        book6 = Book("F. Scott Fitzgerald", "The Great Gatsby", 180)

        self.shelves[0].addBook(book1)
        self.shelves[0].addBook(book2)
        self.shelves[1].addBook(book3)
        self.shelves[1].addBook(book4)
        self.shelves[2].addBook(book5)
        self.shelves[2].addBook(book6)

    def isTherePlaceForNewBook(self):
        for shelf in self.shelves:
            if shelf.isShelfFull == False:
                return True
        return False

    def addNewBook(self, book):
        for shelf in self.shelves:
            if shelf.isShelfFull == False:
                shelf.addBook(book)
                return
        print("No place for new book in the library.")

    def deleteBook(self, title):
        for shelf in self.shelves:
            for i in range(5):
                if shelf.books[i] != None and shelf.books[i].title == title:
                    shelf.books[i] = None
                    shelf.isShelfFull = False
                    return
        print("Book not found.")

    def registerReader(self, name, id):
        new_reader = Reader(id, name)
        self.readers.append(new_reader)

    def removeReader(self, name):
        found = False
        for i in range(len(self.readers)):
            if self.readers[i].name == name:
                del self.readers[i]
                found = True
                break
        if not found:
            print("Reader not found.")

    def searchByAuthor(self, author):
        found_books = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book != None and book.author == author:
                    found_books.append(book.title)
        if len(found_books) == 0:
            print("No books found by this author.")
        else:
            print("Books by", author, ":")
            for title in found_books:
                print(title)
