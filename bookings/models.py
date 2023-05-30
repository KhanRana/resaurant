from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='menu_likes', blank=True)

    def __str__(self):
        return self.title
    
    def num_of_Likes(self):
        return self.likes.count()
    

class Table(models.Model):
    accommodate = (
        ('One', 'One'),
        ('Two', 'Two'),
        ('Four', 'Four'),
        ('Six', 'Six'),
    )
    num = models.PositiveIntegerField()
    capacity = models.CharField(choices=accommodate)

    def __str__(self):
        return f'Table {self.num} can sit {self.capacity}'


TIME_CHOICES = (
    ("6 PM", '1800'),
    ("7 PM", '1900'),
    ("8 PM", '2000'),
    ("9 PM", '2100'),
)

class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    date = models.DateField(default=datetime.now)
    time = models.CharField(choices=TIME_CHOICES)

    def __str__(self):
        return f'''{self.table} and has been booked for {self.date}
        {self.time}'''


class Review(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Review {self.body} by {self.name}'
    
    

    

