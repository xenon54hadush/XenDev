from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True, region = 'ET')
    email = models.EmailField()
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.firstname:
            self.firstname = self.firstname.lower()
        if self.lastname:
            self.lastname = self.lastname.lower()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.firstname.title()} {self.lastname.title()}"


# --- Work Samples ---
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/projects/', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title