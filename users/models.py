from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    """Create user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        # Resizing user profile image for the upload
        # Some of the code was taken from https://stackoverflow.com/users/13449046/takib-ahmed
        # However it has been changed for the project
        super(Profile, self).save()
        # After save, read the file
        image_read = storage.open(self.image.name, "r")
        image = Image.open(image_read)
        if image.height > 200 or image.width > 200:
            size = 200, 200

            # Create a buffer to hold the bytes
            imageBuffer = BytesIO()

            # Resize
            image.thumbnail(size, Image.ANTIALIAS)

            # Save the image as jpeg to the buffer
            image.save(imageBuffer, image.format)

            # Check whether it is resized
            image.show()

            # Save the modified image
            user = Profile.objects.get(pk=self.pk)
            user.image.save(self.image.name, ContentFile(
                imageBuffer.getvalue()))

            image_read = storage.open(user.image.name, "r")
            image = Image.open(image_read)

        image_read.close()
