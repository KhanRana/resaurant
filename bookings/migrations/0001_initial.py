# Generated by Django 4.2.1 on 2023-05-24 13:20

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('price', models.FloatField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('likes', models.ManyToManyField(blank=True, related_name='menu_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]