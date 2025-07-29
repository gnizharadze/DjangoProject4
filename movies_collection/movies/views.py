from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Genre, Director, Movie
from .forms import GenreForm, DirectorForm, MovieForm
from django.contrib.auth.mixins import LoginRequiredMixin



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
    success_url = reverse_lazy('movies:genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('movies:genre_list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'
    success_url = reverse_lazy('movies:genre_list')


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
    success_url = reverse_lazy('movies:director_list')

class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'movies/director_form.html'
    success_url = reverse_lazy('movies:director_list')

class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'movies/director_confirm_delete.html'
    success_url = reverse_lazy('movies:director_list')


# ---------------------------
# MOVIE VIEWS
# ---------------------------

class MovieListView(ListView,LoginRequiredMixin):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query = self.request.GET.get('q')  # საძიებო სიტყვა
        sort = self.request.GET.get('sort')  # დასორტირების ველი
        direction = self.request.GET.get('direction', 'asc')  # default არის ზრდადი

        qs = super().get_queryset()

        if query:
            # საძიებო სიტყვით ფილტრაცია
             qs = qs.filter(
                 Q(title__icontains=query) |
                 Q(description__icontains=query) |
                 Q(genre__name__icontains=query) |
                Q(director__name__icontains=query)
        )

        if sort in ['title', 'release_year', 'genre', 'director']:
            if sort == 'genre':
             order_field = 'genre__name'  # foreign key-ზე დაყრდნობით
            elif sort == 'director':
              order_field = 'director__name'
            else:
              order_field = sort

            if direction == 'desc':
             order_field = '-' + order_field  # კლებადობით დალაგება

             qs = qs.order_by(order_field)

        return qs

class MovieDetailView(DetailView,LoginRequiredMixin):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(CreateView,LoginRequiredMixin):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movies:movie_list')

    # handle file upload
    def form_valid(self, form):
        return super().form_valid(form)

class MovieUpdateView(UpdateView,LoginRequiredMixin):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movies:movie_list')

class MovieDeleteView(DeleteView,LoginRequiredMixin):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movies:movie_list')
