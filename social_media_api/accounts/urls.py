from django.urls import path
from .views import RegisterView, ProfileView, ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
