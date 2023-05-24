from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    price = models.FloatField()
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='menu_likes', blank=True)

    def __str__(self):
        return self.title
    
    def num_of_Likes(self):
        return self.likes.count()
    

