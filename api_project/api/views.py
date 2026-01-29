from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Your existing List View
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer