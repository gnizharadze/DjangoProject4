from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Genre, Director, Movie
from .forms import GenreForm, DirectorForm, MovieForm
from django.db.models import Q

# ---------------------------
# GENRE VIEWS
# ---------------------------

class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'movies/genre_detail.html'
    context_object_name = 'genre'

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')


# ---------------------------
# DIRECTOR VIEWS
# ---------------------------

class DirectorListView(ListView):
    model = Director
    template_name = 'movies/director_list.html'
    context_object_name = 'directors'

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'movies/director_detail.html'
    context_object_name = 'director'

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'movies/director_form.html'
    success_url = reverse_lazy('director_list')

class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'movies/director_form.html'
    success_url = reverse_lazy('director_list')

class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'movies/director_confirm_delete.html'
    success_url = reverse_lazy('director_list')


# ---------------------------
# MOVIE VIEWS
# ---------------------------

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get('q')
        sort = self.request.GET.get('sort')
        direction = self.request.GET.get('direction', 'asc')  # default: ზრდადი
        qs = super().get_queryset()

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(genre__name__icontains=query) |
                Q(director__name__icontains=query)
            )

        if sort in ['title', 'release_year', 'genre', 'director']:
            if sort == 'genre':
                order_field = 'genre__name'
            elif sort == 'director':
                order_field = 'director__name'
            else:
                order_field = sort

            if direction == 'desc':
                order_field = '-' + order_field

            qs = qs.order_by(order_field)

        return qs

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')

    # handle file upload
    def form_valid(self, form):
        return super().form_valid(form)

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

