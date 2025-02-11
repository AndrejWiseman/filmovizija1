from django.db import models
from django.urls import reverse
# from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django.urls import reverse



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
    tags = TaggableManager()
    preporuceno = models.BooleanField(default=False)
    link_gledaj = models.CharField(max_length=200, null=True, blank=True)
    link_preuzmi = models.CharField(max_length=200)

class DomaciFilmovi(models.Model):
    naslov = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    imdb_ocena = models.IntegerField(default=0)
    godina = models.IntegerField(default=0)
    slika = CloudinaryField('image', folder='filmovizija')
    # content = HTMLField()
    opis = models.TextField()
    dodano = models.DateTimeField(auto_now_add=True )
    tags = TaggableManager()
    preporuceno = models.BooleanField(default=False)
    link_gledaj = models.CharField(max_length=200, null=True, blank=True)
    link_preuzmi = models.CharField(max_length=200)

class Serije(models.Model):
    naslov = models.CharField(max_length=120)
    slug = models.SlugField(default="", null=False)
    originalni_naslov = models.CharField(max_length=120, null=False)
    imdb_ocena = models.CharField(max_length=120, null=False)
    godina = models.CharField(max_length=120, null=False, blank=False)
    slika = CloudinaryField('image', folder='filmovizija')
    opis = models.TextField()
    dodano = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    tags = TaggableManager()
    preporuceno = models.BooleanField(default=False)

    def get_episodes_by_season(self):
        episodes = self.epizoda_set.all()
        seasons = {}
        for episode in episodes:
            if episode.sezona not in seasons:
                seasons[episode.sezona] = []
            seasons[episode.sezona].append(episode)
        return seasons
class Epizoda(models.Model):
    epizode = models.ForeignKey(Serije, on_delete=models.CASCADE)
    epizoda_dodano = models.DateField(auto_now_add=True)
    sezona = models.CharField(max_length=120, null=True, blank=True)
    ep = models.CharField(max_length=120, null=True, blank=True)
    link_gledaj = models.CharField(max_length=200, null=True, blank=True)
    link_preuzmi = models.CharField(max_length=200)

    def __str__(self):
        return self.ep




class DomaceSerije(models.Model):
    naslov = models.CharField(max_length=120)
    slug = models.SlugField(default="", null=False)
    imdb_ocena = models.CharField(max_length=120, null=False)
    godina = models.CharField(max_length=120, null=False, blank=False)
    slika = CloudinaryField('image', folder='filmovizija')
    opis = models.TextField()
    dodano = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    tags = TaggableManager()
    preporuceno = models.BooleanField(default=False)

    def get_episodes_by_season(self):
        # episodes = self.epizoda_set.all()
        episodes = self.domaciepizoda_set.all()
        seasons = {}
        for episode in episodes:
            if episode.sezona not in seasons:
                seasons[episode.sezona] = []
            seasons[episode.sezona].append(episode)
        return seasons

class DomaciEpizoda(models.Model):
    epizode = models.ForeignKey(DomaceSerije, on_delete=models.CASCADE)
    epizoda_dodano = models.DateField(auto_now_add=True)
    sezona = models.CharField(max_length=120, null=True, blank=True)
    ep = models.CharField(max_length=120, null=True, blank=True)
    link_gledaj = models.CharField(max_length=200, null=True, blank=True)
    link_preuzmi = models.CharField(max_length=200)

    def __str__(self):
        return self.ep
