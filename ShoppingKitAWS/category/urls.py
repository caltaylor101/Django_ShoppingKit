from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('create-category/', views.create_category, name='category'),
    path('create-private-category/', views.create_private_category, name='private_category'),
    path('private-category/<int:pk>/', views.private_category_view, name='private_category_view'),
    path('private-category/', views.private_category_view, name='private_category_view_no_pk'),
    path('<int:pk>/', views.category_view, name='category_view'),
    path('browse/', views.browse_categories, name='browse_categories'),
    path('join-private-category/', views.join_private_category, name='join_private_category'),
    path('private-category-login/<int:pk>/', views.private_category_login, name='private_category_login'),
    path('private-category-login/', views.private_category_login, name='private_category_login_no_pk')
    
]

