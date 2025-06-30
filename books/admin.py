from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year', 'average_rating', 'created_at', 'updated_at')
    readonly_fields = ('average_rating',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'updated_at')

admin.site.register(BookAuthor)
admin.site.register(BookReview)
