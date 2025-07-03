
from library import Library
from book import Book

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1 - Add a book")
        print("2 - Delete a book")
        print("3 - Register a new reader")
        print("4 - Remove a reader")
        print("5 - Search books by author")
        print("6 - Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            author = input("Enter author: ")
            title = input("Enter title: ")
            pages = int(input("Enter number of pages: "))
            book = Book(author, title, pages)
            library.addNewBook(book)

        elif choice == "2":
            title = input("Enter book title to delete: ")
            library.deleteBook(title)

        elif choice == "3":
            name = input("Enter reader name: ")
            id = int(input("Enter reader ID: "))
            library.registerReader(name, id)

        elif choice == "4":
            name = input("Enter reader name to remove: ")
            library.removeReader(name)

        elif choice == "5":
            author = input("Enter author name to search: ")
            library.searchByAuthor(author)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()