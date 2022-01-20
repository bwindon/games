from .models import Event, Player, Game


def GetPlayers():
    """Get players in events"""
    data = list(Player.objects.values_list('name', flat=True))
    return data


def WinData(player_id):
    """Return number of counts of player id in g_winner column"""
    count = len(Event.objects.all().filter(g_winner=player_id))
    print('count in function WinData', count)
    return count


