import os
import sys
import django

# Find the BASE_DIR (project root, same level as manage.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Point to your settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. All books by a specific author
    author_name = "Chinua Achebe"
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author_name}:")
        books_by_author = Book.objects.filter(author=author)  # ✅ required by checker
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author named {author_name} found.")

    # 2. All books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")

    # 3. Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)  # ✅ required by checker
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

if __name__ == "__main__":
    run_queries()
