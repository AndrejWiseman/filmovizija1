from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Filmovi(models.Model):
    naslov = models.CharField(max_length=100)
    slika = CloudinaryField('image', folder='filmovizija')
