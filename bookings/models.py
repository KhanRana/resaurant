from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
    num = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.num} has {self.capacity}'


class Booking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=20)
    no_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'''Table for {self.no_of_persons} has been booked on {self.date}
        {self.time}'''


class Review(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Review {self.body} by {self.name}'
    
    

    

