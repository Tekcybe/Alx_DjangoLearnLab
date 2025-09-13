
# Register your models here.
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser   # from bookshelf.models


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # show these columns in list view
    list_filter = ("publication_year", "author")             # add filter sidebar
    search_fields = ("title", "author")                      # enable search bar
