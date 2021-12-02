from django.shortcuts import render
from .models import Screening

# Create your views here.


def home(request):
    movies = Screening.objects.all()
    return render(request, 'cinema/home.html', {
        'movies': movies
    })

def show_movie(request, id):
    return render(request, 'cinema/home.html')