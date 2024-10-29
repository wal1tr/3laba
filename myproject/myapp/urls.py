from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.filter_by_genre, name='filter_by_genre'),
]