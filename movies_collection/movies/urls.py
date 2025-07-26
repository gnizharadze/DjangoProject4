from django.urls import path
from . import views

urlpatterns = [
    # Genres
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genres/add/', views.GenreCreateView.as_view(), name='genre_add'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre_edit'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),

    # Directors
    path('directors/', views.DirectorListView.as_view(), name='director_list'),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view(), name='director_detail'),
    path('directors/add/', views.DirectorCreateView.as_view(), name='director_add'),
    path('directors/<int:pk>/edit/', views.DirectorUpdateView.as_view(), name='director_edit'),
    path('directors/<int:pk>/delete/', views.DirectorDeleteView.as_view(), name='director_delete'),

    # Movies
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('movies/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
]
