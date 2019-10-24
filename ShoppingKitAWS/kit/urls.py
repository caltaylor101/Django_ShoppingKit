from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('create-kit', views.post, name='create-kit'),
    path('kit/', views.viewkit, name='viewkit'),
    path('kit/<int:pk>/', views.viewkit, name='viewkit_with_pk'),
    path('test/', views.testingcomments, name='testingcomments'),
    path('test/<int:id>/', views.testingcomments, name='testingcomments_with_id'),
    path('upvote/', views.upvote, name='upvote'),
    path('downvote/', views.downvote, name='downvote'),
    path('upvote_post/', views.upvote_post, name='upvote_post'),
    path('downvote_post/', views.downvote_post, name='downvote_post'),
    path('sort_comments/',views.sort_comments,name='sort_comments'),
]