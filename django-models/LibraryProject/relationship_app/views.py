from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Book   # keep Book separate
from .models import Library   # add Library separately

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ fixed path

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ fixed path
    context_object_name = "library"
