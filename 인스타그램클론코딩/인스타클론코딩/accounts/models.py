from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


def profile_image_path(instance, filename):
    return f'profile/images/{filename}'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    introduction = models.TextField()
    image_file = ProcessedImageField(
        upload_to = profile_image_path,
        processors = [Thumbnail(300, 300)],
        format = 'JPEG',
        options = {'quality': 90},
    )