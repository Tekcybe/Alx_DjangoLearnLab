from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # import the entire views module

urlpatterns = [
    # Existing views
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication views
    path("register/", views.register_view, name="register"),  # checker expects views.register_view
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
