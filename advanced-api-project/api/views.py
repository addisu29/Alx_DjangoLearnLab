from rest_framework import generics, filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    # The BookListView allows for listing books with advanced filtering, searching, and ordering.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Setup Filter Backends
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Step 1: Filtering configuration
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Step 2: Search configuration
    search_fields = ['title', 'author__name']

    # Step 3: Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']