from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class OtherUsers(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.username

class PetGender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PetData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    name = models.CharField(max_length=50)
    gender = models.ForeignKey(PetGender, on_delete=models.RESTRICT)
    contact_number = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.name} {self.contact_email} {self.contact_number} {self.id}'