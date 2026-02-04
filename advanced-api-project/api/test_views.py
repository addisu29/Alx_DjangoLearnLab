from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(
            title='Harry Potter',
            publication_year=1997,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        # Test that any user can list books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        # Test creating a book while logged in
        self.client.login(username='testuser', password='password123')
        data = {'title': 'New Book', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        # Test that unauthenticated users cannot create books
        data = {'title': 'Unauthorized', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Updated Title', 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Harry Potter'})
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        Book.objects.create(title='A Brief History', publication_year=1988, author=self.author)
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.data[0]['title'], 'A Brief History')