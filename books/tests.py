from django.test import TestCase
from django.urls import reverse

from books.models import Book
from users.models import CustomUser


class BooksTestCase(TestCase):
    """
    Test cases for listing and searching books.
    """

    def test_no_books(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No books found.")

    def test_books_list_with_pagination(self):
        books = [
            Book.objects.create(title=f"Book{i}", description=f"Description{i}", isbn=f"00000{i}")
            for i in range(1, 4)
        ]

        # First page: should contain Book1 and Book2
        response = self.client.get(reverse("books:list") + "?page_size=2")
        self.assertContains(response, books[0].title)
        self.assertContains(response, books[1].title)
        self.assertNotContains(response, books[2].title)

        # Second page: should contain Book3
        response = self.client.get(reverse("books:list") + "?page=2&page_size=2")
        self.assertContains(response, books[2].title)

    def test_book_detail_page(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123121")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        sport = Book.objects.create(title="Sport", description="Desc", isbn="001")
        guide = Book.objects.create(title="Guide", description="Desc", isbn="002")
        shoe = Book.objects.create(title="Shoe Dog", description="Desc", isbn="003")

        response = self.client.get(reverse("books:list") + "?q=sport")
        self.assertContains(response, sport.title)
        self.assertNotContains(response, guide.title)
        self.assertNotContains(response, shoe.title)

        response = self.client.get(reverse("books:list") + "?q=guide")
        self.assertContains(response, guide.title)

        response = self.client.get(reverse("books:list") + "?q=shoe")
        self.assertContains(response, shoe.title)


class BookReviewTestCase(TestCase):
    """
    Test case for adding a review to a book.
    """

    def setUp(self):
        self.book = Book.objects.create(title="Book1", description="Description1", isbn="123121")
        self.user = CustomUser.objects.create_user(
            username="fazliddin",
            first_name="Fazliddin",
            last_name="Mamutkhanov",
            email="fmamutkhanov@gmail.com",
            password="password123"
        )

    def test_add_review_authenticated_user(self):
        self.client.login(username="fazliddin", password="password123")
        response = self.client.post(reverse("books:reviews", kwargs={"id": self.book.id}), data={
            "stars_given": 3,
            "comment": "Nice book"
        })

        self.assertEqual(response.status_code, 302)  # Redirect after post
        reviews = self.book.bookreview_set.all()
        self.assertEqual(reviews.count(), 1)
        self.assertEqual(reviews[0].stars_given, 3)
        self.assertEqual(reviews[0].comment, "Nice book")
        self.assertEqual(reviews[0].user, self.user)

    def test_add_review_unauthenticated_user(self):
        response = self.client.post(reverse("books:reviews", kwargs={"id": self.book.id}), data={
            "stars_given": 4,
            "comment": "Anonymous review"
        })

        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

        self.assertEqual(self.book.bookreview_set.count(), 0)
