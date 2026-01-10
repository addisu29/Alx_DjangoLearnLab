from django.contrib import admin
from .models import Book

# Customizing the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Adding a filter sidebar for the publication year
    list_filter = ('publication_year',)
    
    # Adding a search bar for title and author
    search_fields = ('title', 'author')

