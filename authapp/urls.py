from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='authapp/forgot_password.html'
    ), name='forgot_password'),
]
