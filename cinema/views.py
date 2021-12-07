from django.shortcuts import render
from django.db import connection
from .models import Screening, Rooms, Seats, Films, Genres

# Create your views here.


def home(request):
    movies = Screening.objects.all()
    return render(request, 'cinema/home.html', {
        'movies': movies,
    })


def show_movie(request, id):
    movie = Screening.objects.get(id=id)
    seat = Seats.objects.get(id=id)
    # room = Rooms.objects.get(id=id)
    # A = Seats.objects.values_list('row', flat=True)
    A = Seats.objects.filter(row__startswith ='A')
    B = Seats.objects.filter(row__startswith ='B')
    C = Seats.objects.filter(row__startswith ='C')
    D = Seats.objects.filter(row__startswith ='D')
    E = Seats.objects.filter(row__startswith ='E')
    F = Seats.objects.filter(row__startswith ='F')
    G = Seats.objects.filter(row__startswith ='G')
    H = Seats.objects.filter(row__startswith ='H')
    I = Seats.objects.filter(row__startswith ='I')
    J = Seats.objects.filter(row__startswith ='J')
    K = Seats.objects.filter(row__startswith ='K')
    L = Seats.objects.filter(row__startswith ='L')
    M = Seats.objects.filter(row__startswith ='M')
    N = Seats.objects.filter(row__startswith ='N')
    O = Seats.objects.filter(row__startswith ='O')
    P = Seats.objects.filter(row__startswith ='P')
    # B = Seats.objects.filter(row__endswith ='H')&Seats.objects.values_list('number', flat=True)
    # B = Seats.objects.filter(row__startswith ='A').union(Rooms.objects.filter(id=1))
    # B = Seats.objects.filter(row__startswith ='E')
    # for s in Seats.objects.raw("SELECT * FROM cinema_seats WHERE row='A' LIMIT 16"):
    #     print(s)
    seats = Seats.objects.all()
    print(connection.queries)
    return render(request, 'cinema/show_movie.html', {
        'movie': movie,
        'seat': seat,
        # 'room': room,
        'seats': seats,
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'E': E,
        'F': F,
        'G': G,
        'H': H,
        'I': I,
        'J': J,
        'K': K,
        'L': L,
        'M': M,
        'N': N,
        'O': O,
        'P': P,
    })

