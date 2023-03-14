import datetime

from rest_framework import serializers
from .models import Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        # depth = 1


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1

    def validate(self, attrs):
        if attrs['year'] > datetime.date.today().year:
            raise serializers.ValidationError({"year": "Must be <= current year"})
        elif attrs['year'] < 0:
            raise serializers.ValidationError({"year": "Must be +"})
        return attrs

    def create(self, validated_data):
        genre_instance = validated_data.pop('genre')
        genre = Genre.objects.filter(name=genre_instance['name'])
        if not genre:
            Genre.objects.create(**genre_instance)
            genre = Genre.objects.filter(name=genre_instance['name'])
        book_instance = Book.objects.create(genre=genre[0], **validated_data)
        return book_instance
