from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.loginUser, name='loginUser'),
    path('logout/',views.logoutUser, name='logout'),
    path('password/',auth_views.PasswordChangeView.as_view(template_name = 'users/change_password.html'),name='password_change'),
    path('password_change/',auth_views.PasswordChangeDoneView.as_view(template_name = 'users/password_change_complete.html'),name= 'password_change_done'),
    path('userprofile/<str:username>',views.userProfile, name = 'userProfile')
]
