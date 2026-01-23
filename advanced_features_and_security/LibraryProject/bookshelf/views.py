from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def form_example(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})