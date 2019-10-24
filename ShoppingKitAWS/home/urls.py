from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from home.views import HomeView


urlpatterns = [
    path('profile/', HomeView.as_view(), name='profile'),
    path('home/', views.home, name='home'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'), 
    path('', views.homepage, name='homepage')
]