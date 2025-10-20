from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

def profile_pics(instance, filename):
    ext = filename.split('.')[-1].lower()
    return f'uploads/images/{timezone.now().date().isoformat()}/{uuid.uuid4().hex}.{ext}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    image = models.ImageField(upload_to=profile_pics, default='default.jpg')

    def __str__(self):
        return self.user.username
