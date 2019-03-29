from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch', views.fetch, name='fetch'),
    path('drop', views.drop, name='drop'),
    path('search', views.search, name='search')
]