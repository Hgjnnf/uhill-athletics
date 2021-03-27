from django.db import models
from .choices import room_choices



# Create your models here.
class BookingData(models.Model):
    first_name = models.CharField(null=True, blank=False, max_length=30)
    last_name = models.CharField(null=True, blank=False, max_length=30)
    email = models.EmailField(null=True, blank=False, max_length=30)
    room = models.CharField(choices=room_choices, default='Gym', max_length=30)
    date = models.DateField(null=True, blank=False)
    book_from = models.TimeField(null=True, blank=False)
    book_until = models.TimeField(null=True, blank=False)
    comments = models.TextField(null=True, blank=True)

    objects = models.Manager()



    
