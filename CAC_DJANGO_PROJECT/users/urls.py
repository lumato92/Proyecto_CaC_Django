from django.urls import path
from users.views import profile, RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
