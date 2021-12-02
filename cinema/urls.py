from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("show_movie/<int:id>/", views.show_movie, name='show_movie'),
]