

from django.db import models
from django.urls import reverse
# from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField



class Zanrovi(models.Model):
    zanr = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.zanr


class Filmovi(models.Model):
    naslov = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    originalni_naslov = models.CharField(max_length=100)
    imdb_ocena = models.IntegerField(default=0)
    godina = models.IntegerField(default=0)
    slika = CloudinaryField('image', folder='filmovizija')
    # content = HTMLField()
    opis = models.TextField()
    dodano = models.DateTimeField(auto_now_add=True )
    zanrovi = models.ManyToManyField(Zanrovi, related_name="filmovi")
    # tags = TaggableManager()
    preporuceno = models.BooleanField(default=False)
    link_gledaj = models.CharField(max_length=200)
    link_preuzmi = models.CharField(max_length=200)

    def __str__(self):
        return self.naslov

    # def get_absolute_url(self):
    #         return reverse('film-detaljno', kwargs={'slug': self.slug})

