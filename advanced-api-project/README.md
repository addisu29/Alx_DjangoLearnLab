
## Testing Strategy

To ensure API reliability, the following tests were implemented in `api/test_views.py`:
- **CRUD Operations**: Verified creation, retrieval, updates, and deletion.
- **Permissions**: Confirmed that only authenticated users can modify data while others can only read.
- **Filtering & Searching**: Verified query parameters work as expected.

### How to run tests:
```bash
python3 manage.py test api
```