from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='menu_likes', blank=True)

    def __str__(self):
        return self.title
    
    def num_of_Likes(self):
        return self.likes.count()
    
class Review(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Review {self.body} by {self.name}'
    
    

    

