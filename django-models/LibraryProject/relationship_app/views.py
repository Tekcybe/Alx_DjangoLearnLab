from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Book
from .models import Library

# ----------------------------
# User Registration View
# ----------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("list_books")  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# ----------------------------
# User Login View
# ----------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# ----------------------------
# User Logout View
# ----------------------------
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ fixed path

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ fixed path
    context_object_name = "library"
