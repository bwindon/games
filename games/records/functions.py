from records.models import Player, Event, Game
import pandas as pd


def CreatePlayerDataFrame(pl):
    """DF that queries player results and played data to build results frame"""

    opponent_qs = GetOpponents(pl)
    game_qs = Game.objects.all()
    col_num = len(game_qs) * 4
    print(col_num)

    """Create a list of opponents and player_df with on column list of opponents"""
    data = [
        {'opponent': q.name}
        for q in opponent_qs
    ]
    player_df = pd.DataFrame(data, columns=['opponent'])

    """loop to create column names by game in sets of 4:
    wins, played, ratio, opponent wins"""
    for gm in game_qs:
        col_n = gm.g_code
        col_ns = str(col_n)
        col_name_a = col_ns + 'w'
        col_name_b = col_ns + 'p'
        col_name_c = col_ns + 'r'
        col_name_d = col_ns + 'ow'
        player_data_array = []

        """Loop to get data for columns and develop the full dataframe"""
        for opponent in opponent_qs:
            player_data_qs = PlayerData(pl, gm, opponent)
            player_data_array.append(player_data_qs)
            player_df[[col_name_a, col_name_b, col_name_c, col_name_d]] = pd.DataFrame(player_data_array)

    return player_df


def EventFilter(g_players, g_name):
    qs = Event.objects.all().filter(g_players).filter(g_name)
    return qs


def GetOpponents(player):
    """Get opponents of player parameter in events"""

    data_qs = list(Player.objects.exclude(id=player))
    return data_qs


def GetPlayers():
    """Get players in events"""
    data_qs = list(Player.objects.all())
    return data_qs


def GetPlayerIDs():
    """return a list of player IDs"""
    ordered_player_id_qs = Player.objects.order_by('id').values_list('id', flat=True)
    return ordered_player_id_qs


def PlayerWinsCountQS():
    id_list = GetPlayerIDs()
    p_win_qs = []
    for x in id_list:
        p_wins = WinCount(x)
        p_win_qs.append(p_wins)
    return p_win_qs


def WinCount(player_id):
    """Return number of counts of player id in g_winner column"""
    count = len(Event.objects.all().filter(g_winner=player_id))
    return count


def PlayerPlayedCountQS():
    id_list = GetPlayerIDs()
    p_played_qs = []
    for x in id_list:
        p_played = PlayedCount(x)
        p_played_qs.append(p_played)
    return p_played_qs


def PlayedCount(player_id):
    """Return number of counts of player id in players column"""
    count = len(Event.objects.all().filter(g_players=player_id))
    return count


def PlayerData(player, game, opponent):
    '''cretae a filterset to eclude others'''
    qs = Event.objects.filter(g_players=player).filter(g_name=game).filter(g_players=opponent).exclude(multi_player=True)
    """an option to remove multiplayer. Player x and y with no other player, add and attribute on the model"""
    count_wins = len(qs.filter(g_winner=player))
    count_played = len(qs.filter(g_players=player))
    opponent_wins = count_played - count_wins

    if count_played == 0:
        win_ratio = 'na'
    else:
        win_ratio = count_wins/count_played

    return count_wins, count_played, win_ratio, opponent_wins


def PlayerDataComprehensive(player, game):
    """player data by game iterated by opponent"""
    # game = [1]
    # player =1
    opponents = Player.objects.all().exclude(id=player)
    print('opponents ', opponents)
    count_wins_qs = []
    count_played_qs = []
    win_ratio_qs = []
    i = 0
    for opponent in opponents:
        i = i + 1
        qs = Event.objects.filter(g_players=player).filter(g_name=game).filter(g_players=opponent)
        print(qs)
        count_wins = len(qs.filter(g_winner=player))
        count_played = len(qs.filter(g_players=player))
        count_wins_qs.append(count_wins)
        count_played_qs.append(count_played)

        if count_played == 0:
            win_ratio = 'na'
            win_ratio_qs.append(win_ratio)
        else:
            win_ratio = count_wins / count_played
            win_ratio_qs.append(win_ratio)

    return count_wins_qs, count_played_qs, win_ratio_qs


def CreatePlayerDataTableByGame(player, game):
    """A framing funtion to query counts and return a table of results by player"""