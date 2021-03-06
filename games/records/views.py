import json
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django_tables2 import SingleTableView, SingleTableMixin
from .tables import EventTable, PlayerTable
from .functions import *
from django.views.generic import CreateView, DetailView
from .forms import EventForm, PlayerForm, GameForm, PlayerDataSelectForm
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import EventFilter
from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from django.urls import reverse


def DataFrameToListView(request,pl):
    pl = 1
    player_df_test = DataFrameToList()
    # compile dictionary and pass to template
    df_dict = {
        "df": player_df_test
    }
    return render(request, 'panda.html', context=df_dict)


def SelectChart(request):
    player_df = None
    op_list = None
    w_data = None
    p_data = None
    ow_data = None

    search_form = PlayerDataSelectForm(request.POST or None)

    if request.method == 'POST':
        pl = request.POST.get('name')
        gm = request.POST.get('game')
        chart = request.POST.get('chart')
        if chart == '1':
            chart_type = 'google-chart'
        elif chart == '2':
            chart_type = 'chart-results'
        else:
            chart_type = 'google-dashboard'

        player_df = CreatePlayerDataFrame(pl)

        if len(player_df) > 0:

            return HttpResponseRedirect(reverse(chart_type, args=(pl, gm)))

        else:
            messages.warning(request, "Apparently no data available...")

    context = {
        'search_form': search_form
    }
    return render(request, 'chart_results_select.html', context)


def DataframeDashboardStackedView(request, pl):

    # h_var : The title for horizontal axis
    h_var = 'opponent'
    h_var_json = json.dumps(h_var)

    # v_var : The title for horizontal axis
    v_var = 'wins'
    v_var_json = json.dumps(v_var)
    v_var2 = 'opponent wins'

    full_data = DataFrameToStackedList(pl)
    full_data_json = json.dumps(full_data)

    values = [
        ["opponent", "wins", "opponent wins"],
        ["Brad - m", 4, 2],
        ["Brad - s", 0, 1],
        ["Rob - m", 1, 4],
        ["Rob - s", 1, 4],
        ["Rob - d", 1, 4],
        ["Rob - x", 1, 4],
    ]

    return render(request, 'dataframe_dashboard_stacked.html', {'values': values, 'h_title': h_var_json,'v_title': v_var_json})


def DataframeDashboardView(request, pl):

    # h_var : The title for horizontal axis
    h_var = 'opponent'
    h_var_json = json.dumps(h_var)

    # v_var : The title for horizontal axis
    v_var = 'wins'
    v_var_json = json.dumps(v_var)
    v_var2 = 'opponent wins'

    full_data = DataFrameToList(pl)
    full_data_json = json.dumps(full_data)
    print(full_data_json)
    return render(request, 'dataframe_dashboard.html', {'values': full_data_json, 'h_title': h_var_json,'v_title': v_var_json})


def GoogleDashboardView(request, pl, gm):
    gm = 1
    """Get player dataframe and parse data for chart"""
    player_df = CreatePlayerDataFrame(pl)

    """get player name for chart label"""
    qs = Player.objects.filter(id=pl)
    for pl_name in qs:
        pl_name.name
    print(pl_name)

    """Get g_code prefix for list making"""
    g_code_prefix = Game.objects.filter(id=gm)
    for gm in g_code_prefix:
        w = gm.g_code + 'w'
        p = gm.g_code + 'p'
        ow = gm.g_code + 'ow'

    """Create lists for chart"""
    op_list = player_df.opponent.tolist()
    w_data = player_df[str(w)].tolist()
    p_data = player_df[str(p)].tolist()
    ow_data = player_df[str(ow)].tolist()

    # h_var : The title for horizontal axis
    h_var = 'opponent'

    # v_var : The title for horizontal axis
    v_var = 'wins'
    v_var2 = 'opponent wins'
    # data : A list of list which will ultimated be used
    # to populate the Google chart.

    data = [[h_var, v_var, v_var2]]
    l = len(op_list)
    for i in range(0, l):
        data.append([op_list[i], w_data[i], ow_data[i]])

    data_json = json.dumps(data)
    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)
    print('data JSON', data_json)

    return render(request, 'google_dashboard.html', {'values': data_json, 'h_title': h_var_JSON,'v_title': v_var_JSON})


def GoogleChartResultsView(request, pl, gm):

    """Get player dataframe and parse data for chart"""
    player_df = CreatePlayerDataFrame(pl)

    """get player name for chart label"""
    qs = Player.objects.filter(id=pl)
    for pl_name in qs:
        pl_name.name
    print(pl_name)

    """Get g_code prefix for list making"""
    g_code_prefix = Game.objects.filter(id=gm)
    for gm in g_code_prefix:
        w = gm.g_code + 'w'
        p = gm.g_code + 'p'
        ow = gm.g_code + 'ow'

    """Create lists for chart"""
    op_list = player_df.opponent.tolist()
    w_data = player_df[str(w)].tolist()
    p_data = player_df[str(p)].tolist()
    ow_data = player_df[str(ow)].tolist()

    # h_var : The title for horizontal axis
    h_var = 'opponent'

    # v_var : The title for horizontal axis
    v_var = 'wins'
    v_var2 = 'opponent wins'
    # data : A list of list which will ultimated be used
    # to populate the Google chart.

    data = [[h_var, v_var, v_var2]]
    l = len(op_list)
    for i in range(0, l):
        data.append([op_list[i], w_data[i], ow_data[i]])

    data_json = json.dumps(data)
    h_var_JSON = json.dumps(h_var)
    v_var_JSON = json.dumps(v_var)
    print('data json ob working chart ', data_json)
    return render(request, 'google_chart.html', {'values': data_json, 'h_title': h_var_JSON,'v_title': v_var_JSON})


def ChartResultsView(request, pl, gm):

    """Get player dataframe and parse data for chart"""
    player_df = CreatePlayerDataFrame(pl)

    """get player name for chart label"""
    qs = Player.objects.filter(id=pl)
    for pl_name in qs:
        pl_name.name
    print(pl_name)

    """Get g_code prefix for list making"""
    g_code_prefix = Game.objects.filter(id=gm)
    for gm in g_code_prefix:
        w = gm.g_code + 'w'
        p = gm.g_code + 'p'
        ow = gm.g_code + 'ow'

    """Create lists for chart"""
    op_list = player_df.opponent.tolist()
    w_data = player_df[str(w)].tolist()
    p_data = player_df[str(p)].tolist()
    ow_data = player_df[str(ow)].tolist()


    """Compile dictionary for chart"""
    df_dict = {
        'player_df': player_df,
        'op_list': op_list,
        'w_key': w_data,
        'p_key': p_data,
        'ow_key': ow_data,
        'pl_name': pl_name,
        'gm': gm,
    }

    return render(request, 'chart_player_results.html', context=df_dict)


def ChartView(request):
    qs = Game.objects.all().values()
    df = pd.DataFrame(qs)
    print(df)
    df1 = df.g_code.tolist()
    print(df1)
    no =[]
    x=0
    for item in qs:
        x = x +1
        no.append(x)
    mydict = {
        'df1': df1,
    }
    return render(request, 'chart.html', context=mydict)


def PandaResultsView(request, pl):
    """Get player results dataframe and parse data for html"""

    player_df_test = CreatePlayerDataFrame(pl)
    # compile dictionary and pass to template
    df_dict = {
        "df": player_df_test.to_html()
    }
    return render(request, 'panda.html', context=df_dict)


def PandasWinnerView(request, pl, gm, op):
    """DF displaying players and winners"""

    # get filtered objects from Event model and create initial DataFrame
    played_qs = Event.objects.filter(g_players=pl).filter(g_name=gm).filter(g_players=op)
    data = [
        {'id':q.pk, 'game': q.g_name, 'players': [p.name for p in q.g_players.all()], 'winner':q.g_winner}
        for q in played_qs
    ]
    player_df = pd.DataFrame(data, columns=['id', 'game', 'players', 'winner'])
    result = player_df['winner'].value_counts()
    result2 = player_df['players'].value_counts()
    result3 = player_df['game'].value_counts()
    print('result ', result)
    print('result 2 ', result2)
    print('result 3', result3)
    # compile dictionary and pass to template
    dict = {
        "df": player_df.to_html()
    }
    return render(request, 'panda.html', context=dict)


def PlayerDataTotalsView(request):
    """Shell view for retrieving objects"""

    """ THIS is where the filters need to be applied"""

    player_wins_qs = PlayerWinsCountQS()
    print('player_wins_qs = ', player_wins_qs)
    player_played_qs = PlayerPlayedCountQS()
    print('player_played_qs = ', player_played_qs)

    players = Player.objects.all()
    i = 0
    for obj in players:
        obj.name
        obj.wins = player_wins_qs[i]
        obj.played = player_played_qs[i]
        obj.random_label = 'random label'
        if player_played_qs[i]==0:
            obj.percent = 'na'
        else:
            obj.percent = player_wins_qs[i]/player_played_qs[i]
        i = i + 1
    return render(request, 'data.html', {'data': players})


def home(request):
    return render(request, 'home.html', {})


'''
pivot views
'''

def menu(request):
    return HttpResponse("This is the beginning of a menu page")


class EventList(SingleTableMixin, FilterView):
    """The main event list view"""
    model = Event
    table_class = EventTable
    template_name = 'event_list.html'
    filterset_class = EventFilter


class EventListSimple(ListView):
    """An example of a ListView based on a model - not required"""
    model = Event
    table_class = EventTable
    template_name = 'event_list_simple.html'


class PlayerList(SingleTableView):
    """An example of a single table view - not required"""
    model = Player
    table_class = PlayerTable
    template_name = 'event_list.html'


class EventDetailView(DetailView):
    """Displays a page of event details by event ID"""
    model = Event
    fields = ('g_name', 'g_date', 'g_location', 'g_tag', 'g_players', 'g_notes', 'g_winner')


"""
Forms - two types. 
First based on create view CLASS. Harder to pass list to template.
Second based on a view FUNCTION that calls EventForm CLASS. Allows the function to pass list to template
"""


class EventCreateView(CreateView):

    model = Event
    form_class = EventForm
    success_url = reverse_lazy('menu')


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('menu')


"""Form views with lists"""


def EventFormView(request):
    objs = Event.objects.all()

    # create object of form
    form = EventForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    form = EventForm()

    return render(request, 'event_form.html', {'form': form, 'objs': objs})


def PlayerFormView(request):
    objs = Player.objects.all()

    # create object of form
    form = PlayerForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    form = PlayerForm()

    return render(request, 'player_form.html', {'form': form, 'objs': objs})


def GameFormView(request):
    objs = Game.objects.all()

    # create object of form
    form = GameForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    form = GameForm()

    return render(request, 'game_form.html', {'form': form, 'objs': objs})






