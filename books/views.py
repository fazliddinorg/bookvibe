from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import Book, BookReview


class BooksView(View):
    def get(self, request):
        search_query = request.GET.get('q', '')
        books = Book.objects.all().order_by('id')

        if search_query:
            books = books.filter(title__icontains=search_query)

        try:
            page_size = int(request.GET.get('page_size', 4))
        except ValueError:
            page_size = 4

        paginator = Paginator(books, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            "books/list.html",
            {
                "page_obj": page_obj,
                "search_query": search_query
            }
        )


class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        review_form = BookReviewForm()
        return render(
            request,
            "books/detail.html",
            {"book": book, "review_form": review_form}
        )


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                **review_form.cleaned_data
            )
            messages.success(request, "Your review has been added.")
            return redirect(reverse("books:detail", kwargs={"id": book.id}))

        return render(request, "books/detail.html", {"book": book, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(book.bookreview_set, id=review_id)
        review_form = BookReviewForm(instance=review)

        return render(request, "books/edit_review.html", {
            "book": book,
            "review": review,
            "review_form": review_form
        })

    def post(self, request, book_id, review_id):
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(book.bookreview_set, id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            messages.success(request, "Your review has been updated.")
            return redirect(reverse("books:detail", kwargs={"id": book.id}))

        return render(request, "books/edit_review.html", {
            "book": book,
            "review": review,
            "review_form": review_form
        })


class ConfirmDeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(book.bookreview_set, id=review_id)

        return render(request, "books/confirm_delete_review.html", {
            "book": book,
            "review": review
        })


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(book.bookreview_set, id=review_id)

        review.delete()
        messages.success(request, "You have successfully deleted this review.")
        return redirect(reverse("books:detail", kwargs={"id": book.id}))
