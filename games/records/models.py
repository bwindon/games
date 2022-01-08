from django.db import models

# Create your models here.


class Player(models.Model):
    """Players attending game event"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    """
    Game info
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Result(models.Model):
    """"List of winners for an event"""
    winners = models.ManyToManyField(Player, verbose_name='Players')

    def __int__(self):
        return self.winners


class Event(models.Model):
    """
    A game event instance
    """

    g_name = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Game Name')
    g_date = models.DateTimeField(verbose_name='Date')
    g_location = models.CharField(default='NA', max_length=100, verbose_name='location')
    g_tag = models.CharField(default='NA', max_length=100, verbose_name='Descriptor')
    g_players = models.ManyToManyField(Player, verbose_name='Players')
    g_notes = models.TextField(null=True, verbose_name='Notes')
    g_result = models.ForeignKey(Result, null=True, on_delete=models.CASCADE, verbose_name='Winners')

    def __int__(self):
        return self.g_name
