from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse



urlpatterns = [
    
    
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile' ),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
    # path('reset-password-email/', views.reset_password_email, name='reset-password-email')

]