from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from books.models import BookReview
from api.serializers import BookReviewSerializer


class BookReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit book reviews.
    Only authenticated users can access.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    lookup_field = 'id'

    def get_queryset(self):
        # Optionally limit to only current user's reviews:
        return BookReview.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically assign current user
        serializer.save(user=self.request.user)
