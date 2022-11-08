from django.db import models
from django.conf import settings

# Create your models here.
def posts_image_path(instance, filename):
    return f'images/{filename}'


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to=posts_image_path)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()