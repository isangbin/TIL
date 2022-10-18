from django.db import models

# Create your models here.
def posts_image_path(instance, filename):
    return f'images/{filename}'


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to=posts_image_path)