from django.db import models
from django.utils import timezone
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=120,
                                verbose_name="artist")

    class Meta:
        verbose_name = "artist"


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artist',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=220)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    milliseconds = models.TextField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.name