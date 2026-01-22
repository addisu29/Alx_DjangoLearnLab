# Permissions and Groups Setup

## Groups:
1. **Viewers**: Assigned 'can_view' permission. Can only see the book list.
2. **Editors**: Assigned 'can_view', 'can_create', and 'can_edit' permissions.
3. **Admins**: Assigned all permissions ('can_view', 'can_create', 'can_edit', 'can_delete').

## Implementation:
- Custom permissions are defined in the `Book` model's `Meta` class.
- Views are protected using the `@permission_required` decorator.
- These groups should be created via the Django Admin panel or a setup script.
