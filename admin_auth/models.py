from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import uuid


def image_upload(instance, filename):
    ext = filename.split('.')[-1].lower()
    return f'uploads/images/{timezone.now().date().isoformat()}/{uuid.uuid4().hex}.{ext}'




class AdminBoard(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to=image_upload, validators=[FileExtensionValidator(['jpg','jpeg', 'png'])], null=True, blank=True)

