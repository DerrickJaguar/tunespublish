# recommendation/models.py

from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    tempo = models.FloatField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.artist}"

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    play_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.track.title}"

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_genres = models.TextField(blank=True)
    disliked_genres = models.TextField(blank=True)

    def __str__(self):
        return f"Preferences of {self.user.username}"



class Recommendation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    song = models.ForeignKey('musicapp.Song', on_delete=models.CASCADE)  # Assuming songs are managed by 'musicapp'
    recommended_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song} recommended to {self.user.username}"    
