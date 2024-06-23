from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
]