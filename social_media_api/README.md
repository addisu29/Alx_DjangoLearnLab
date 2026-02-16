# Social Media API - Accounts

## Setup
1. Install dependencies: `pip install djangorestframework django-filter pillow`
2. Run migrations: `python manage.py migrate`

## Features
- **Registration**: `POST /api/accounts/register/` - Creates a user and returns a Token.
- **Login**: `POST /api/accounts/login/` - Returns a Token for valid credentials.
- **Profile**: `GET/PUT/PATCH /api/accounts/profile/` - Manage bio and profile picture (Requires Token).

## User Model
Custom user model extending AbstractUser with:
- bio (TextField)
- profile_picture (ImageField)
- followers (ManyToManyField)
