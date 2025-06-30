from rest_framework import serializers
from books.models import Book, BookReview
from users.models import CustomUser

class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn', 'average_rating')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'comment', 'book', 'user', 'user_id', 'book_id')

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        book_id = validated_data.pop('book_id')

        user = CustomUser.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)

        return BookReview.objects.create(user=user, book=book, **validated_data)
