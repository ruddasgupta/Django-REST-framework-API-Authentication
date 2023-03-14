from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import BookFilter
from .models import Book, Genre
from .pagination import CustomPagination
from .serializers import BookSerializer, GenreSerializer


class GenreListView(APIView):
    def get(self, request):
        all_genre = Genre.objects.all()
        serializers = GenreSerializer(all_genre, many=True)
        return Response(serializers.data)


class ListCreateBookAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # permission_classes = [IsAuthenticated]
    # pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


class RetrieveUpdateDestroyBookAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # permission_classes = [IsAuthenticated]