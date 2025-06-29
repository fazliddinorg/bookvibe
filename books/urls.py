from django.urls import path
from books.views import (
    BooksView,
    BookDetailView,
    AddReviewView,
    EditReviewView,
    ConfirmDeleteReviewView,
    DeleteReviewView,
)

app_name = "books"

urlpatterns = [
    path("", BooksView.as_view(), name="book-list"),
    path("<int:id>/", BookDetailView.as_view(), name="book-detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="review-add"),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="review-edit"),
    path("<int:book_id>/reviews/<int:review_id>/delete/confirm/", ConfirmDeleteReviewView.as_view(), name="review-delete-confirm"),
    path("<int:book_id>/reviews/<int:review_id>/delete/", DeleteReviewView.as_view(), name="review-delete"),
]
