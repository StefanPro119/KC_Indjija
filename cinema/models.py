from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField



class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_customer')


class Genres(models.Model):
    name = models.CharField(max_length=15)


class Films(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    picture = ResizedImageField(size=[300, 300], quality=100, null=True, blank=True)
    lenght_min = models.IntegerField()
    genre = models.ManyToManyField(Genres, related_name='gnr')


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    no_seats = models.IntegerField()


class Seats(models.Model):
    row = models.CharField(max_length=2)
    number = models.IntegerField()
    rooms_id = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='rooms_id')


class Screening(models.Model):
    film_id = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='film_id')
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='room_id')
    calendar = models.DateField(null=True)
    start_time = models.TimeField(null=True)