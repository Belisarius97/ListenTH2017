from django.db import models

# Create your models here.

"""
We want a song ID, and so if we hardcode information then...

"""

class Song(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    lyrics = models.TextField()
    spotify_track_id = models.CharField(max_length=100)
    def __str__(self):
        return ("%s | %s | %s" % (self.artist, self.album, self.title))