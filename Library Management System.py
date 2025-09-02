import json
import os

# File to store book records
BOOKS_FILE = "library.json"


class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as f:
                return json.load(f)
        return []

    def save_books(self):
        with open(BOOKS_FILE, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author):
        book = {"title": title, "author": author, "available": True}
        self.books.append(book)
        self.save_books()
        print(f"✅ '{title}' by {author} added successfully!")

    def view_books(self):
        if not self.books:
            print("📂 No books available in the library.")
            return
        print("\n📚 Library Books:")
        for i, book in enumerate(self.books, 1):
            status = "Available" if book["available"] else "Issued"
            print(f"{i}. {book['title']} by {book['author']} - {status}")

    def issue_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and book["available"]:
                book["available"] = False
                self.save_books()
                print(f"📕 '{title}' has been issued.")
                return
        print(f"❌ '{title}' is not available or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["available"]:
                book["available"] = True
                self.save_books()
                print(f"📗 '{title}' has been returned.")
                return
        print(f"❌ '{title}' was not issued from this library.")


def menu():
    library = Library()
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("Enter book title to issue: ")
            library.issue_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
