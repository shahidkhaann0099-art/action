import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book
from member import Member
from issue_return import issue_book, return_book
from search import search_by_title, search_by_author, search_by_isbn
from auth_system import authenticate

user_db = {"admin": "admin123", "user": "user123"}
library = Library()
members = {}

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")
        self.show_login()

    def show_login(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate(username, password, user_db):
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def show_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Library Management System", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Add Book", command=self.add_book_window).pack(fill="x")
        tk.Button(self.root, text="Add Member", command=self.add_member_window).pack(fill="x")
        tk.Button(self.root, text="Issue Book", command=self.issue_book_window).pack(fill="x")
        tk.Button(self.root, text="Return Book", command=self.return_book_window).pack(fill="x")
        tk.Button(self.root, text="Search Book", command=self.search_book_window).pack(fill="x")
        tk.Button(self.root, text="List Books", command=self.list_books_window).pack(fill="x")

    def add_book_window(self):
        self.clear_window()
        tk.Label(self.root, text="Add Book").pack()
        tk.Label(self.root, text="ISBN").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()
        tk.Label(self.root, text="Title").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()
        tk.Label(self.root, text="Author").pack()
        author_entry = tk.Entry(self.root)
        author_entry.pack()
        tk.Label(self.root, text="Copies").pack()
        copies_entry = tk.Entry(self.root)
        copies_entry.pack()
        def add_book_action():
            book = Book(isbn_entry.get(), title_entry.get(), author_entry.get(), int(copies_entry.get()))
            library.add_book(book)
            messagebox.showinfo("Success", "Book added successfully!")
            self.show_main_menu()
        tk.Button(self.root, text="Add", command=add_book_action).pack()

    def add_member_window(self):
        self.clear_window()
        tk.Label(self.root, text="Add Member").pack()
        tk.Label(self.root, text="Member ID").pack()
        id_entry = tk.Entry(self.root)
        id_entry.pack()
        tk.Label(self.root, text="Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        def add_member_action():
            member = Member(id_entry.get(), name_entry.get())
            members[id_entry.get()] = member
            messagebox.showinfo("Success", "Member added successfully!")
            self.show_main_menu()
        tk.Button(self.root, text="Add", command=add_member_action).pack()

    def issue_book_window(self):
        self.clear_window()
        tk.Label(self.root, text="Issue Book").pack()
        tk.Label(self.root, text="Member ID").pack()
        member_entry = tk.Entry(self.root)
        member_entry.pack()
        tk.Label(self.root, text="Book ISBN").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()
        def issue_action():
            member_id = member_entry.get()
            isbn = isbn_entry.get()
            if member_id in members and issue_book(library, isbn, members[member_id]):
                messagebox.showinfo("Success", "Book issued successfully!")
            else:
                messagebox.showerror("Error", "Cannot issue book!")
            self.show_main_menu()
        tk.Button(self.root, text="Issue", command=issue_action).pack()

    def return_book_window(self):
        self.clear_window()
        tk.Label(self.root, text="Return Book").pack()
        tk.Label(self.root, text="Member ID").pack()
        member_entry = tk.Entry(self.root)
        member_entry.pack()
        tk.Label(self.root, text="Book ISBN").pack()
        isbn_entry = tk.Entry(self.root)
        isbn_entry.pack()
        def return_action():
            member_id = member_entry.get()
            isbn = isbn_entry.get()
            if member_id in members and return_book(library, isbn, members[member_id]):
                messagebox.showinfo("Success", "Book returned successfully!")
            else:
                messagebox.showerror("Error", "Cannot return book!")
            self.show_main_menu()
        tk.Button(self.root, text="Return", command=return_action).pack()

    def search_book_window(self):
        self.clear_window()
        tk.Label(self.root, text="Search Book").pack()
        tk.Label(self.root, text="Enter Title").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()
        def search_action():
            results = search_by_title(library, title_entry.get())
            if results:
                books_str = "\n".join([str(b) for b in results])
                messagebox.showinfo("Results", books_str)
            else:
                messagebox.showinfo("Results", "No books found.")
            self.show_main_menu()
        tk.Button(self.root, text="Search", command=search_action).pack()

    def list_books_window(self):
        self.clear_window()
        books = library.list_books()
        if books:
            books_str = "\n".join([str(b) for b in books])
            tk.Label(self.root, text=books_str).pack()
        else:
            tk.Label(self.root, text="No books available").pack()
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
