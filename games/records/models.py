from django.db import models


# Create your models here.
class Player(models.Model):
    """Players attending game event"""
    name = models.CharField(unique=True, max_length=25, verbose_name='Player')


    def __str__(self):
        return self.name


class Game(models.Model):
    """
    Game info
    """
    name = models.CharField(unique=True, max_length=50)
    collab = models.BooleanField(default=False)
    g_code = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.collab, self.g_code)
"""
    def __str__(self):
        return self.name

    def __bool__(self):
        return self.collab
"""

class Event(models.Model):
    """
    A game event instance
    """
    g_name = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Game Name', related_name='Name')
    g_date = models.DateField(verbose_name='Date')
    g_location = models.CharField(default='somewhere', max_length=50, verbose_name='Location')
    g_tag = models.CharField(blank=True, max_length=50, verbose_name='Descriptor')
    g_players = models.ManyToManyField(Player, verbose_name='Players', related_name='Players')
    g_notes = models.CharField(blank=True, null=True, verbose_name='Notes', max_length=100)
    #g_winner = models.ForeignKey(Player, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Winner')
    g_winner = models.ManyToManyField(Player, verbose_name='Winner', related_name='Winner')
    multi_player = models.BooleanField(default=False)

    def __str__(self):
        return 'ID = %s  %s  on  %s at %s - winner - %s' % (self.id, self.g_name, self.g_date, self.g_location, self.g_winner)



#class PlayerRecords(models.Model):
    # player game opponents multi non-multi

