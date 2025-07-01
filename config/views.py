from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from books.models import BookReview


def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, "landing.html")


def home_page(request: HttpRequest) -> HttpResponse:
    book_reviews = BookReview.objects.all().order_by('-created_at')

    try:
        page_size = min(int(request.GET.get('page_size', 10)), 100)
    except ValueError:
        page_size = 10

    paginator = Paginator(book_reviews, page_size)

    try:
        page_num = int(request.GET.get('page', 1))
    except ValueError:
        page_num = 1

    page_obj = paginator.get_page(page_num)

    return render(request, "home.html", {"page_obj": page_obj})
