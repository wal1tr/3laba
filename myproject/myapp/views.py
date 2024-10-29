from django.shortcuts import render
from .models import Movie, Genre

def filter_by_genre(request):
    genre_id = request.GET.get('genre') or request.COOKIES.get('last_genre')
    movies = Movie.objects.filter(genre_id=genre_id) if genre_id else None
    genres = Genre.objects.all()
    response = render(request, 'myapp/index.html', {'movies': movies, 'genres': genres})
    
    if request.GET.get('genre'):
        response.set_cookie('last_genre', genre_id)
    return response