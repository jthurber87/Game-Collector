from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

WINNER = [
    ('J', 'Jay'),
    ('M', 'Mollie'),
    ('A', 'Aja'),
    ('C', 'Calvin')
]


class Game(models.Model):
    name = models.CharField(max_length=(100))
    photos = models.CharField("Photo URL", max_length=(500))
    players = models.CharField("Player count", max_length=(50))
    description = models.TextField(max_length=(250))
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})


class Play(models.Model):
    date = models.DateField("date", default=date.today)
    winner = models.CharField(
            "winner", max_length=1, choices=WINNER, default=WINNER[0][0]
            )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_winner_display()} won on {self.date}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"
