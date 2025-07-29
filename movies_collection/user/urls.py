from django.urls import path
from django.contrib.auth import views as auth_views #logoutistvis
from .views import CustomUsernameLoginView


app_name='user'

urlpatterns=[
    path('logout/',auth_views.LogoutView.as_view(next_page='/user/login/'),name='logout'),
]