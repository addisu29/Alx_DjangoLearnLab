# CRUD Operations Documentation

## Create
Command: Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Output: Successful creation of Book instance.

## Retrieve
Command: Book.objects.get(title="1984")
Output: 1984 by George Orwell, 1949

## Update
Command: book.title = "Nineteen Eighty-Four"; book.save()
Output: Title updated successfully.

## Delete
Command: book.delete()
Output: <QuerySet []> (Confirmation of deletion)
