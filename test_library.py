import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book('123', 'Test Book', 'Author', 2)
        library.add_book(book)
        self.assertIn('123', library.books)

if __name__ == "__main__":
    unittest.main()
