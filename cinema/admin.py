from django.contrib import admin
from .models import Films, Rooms, Seats, Screening, User

# Register your models here.
admin.site.register(Films)
admin.site.register(Rooms)
admin.site.register(Seats)
admin.site.register(Screening)
