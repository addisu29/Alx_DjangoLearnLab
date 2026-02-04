from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enable Filtering, Searching, and Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Define specific fields for filtering (exact matches)
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Define fields for text search (partial matches)
    search_fields = ['title', 'author']
    
    # Define fields allowed for ordering
    ordering_fields = ['title', 'publication_year']
    
    # Set a default ordering
    ordering = ['title']