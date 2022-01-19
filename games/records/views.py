from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event, Result, Player, Game
from django.views.generic import ListView
from django_tables2 import SingleTableView, SingleTableMixin
from .tables import EventTable, ResultTable, PlayerTable
from .functions import GetPlayers
from django.views.generic import CreateView, DetailView
from .forms import EventForm, PlayerForm, GameForm
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import EventFilter
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def menu(request):
    return HttpResponse("This is the beginning of a menu page")


class EventList(SingleTableMixin, FilterView):
    model = Event
    table_class = EventTable
    template_name = 'event_list.html'
    filterset_class = EventFilter


class EventListSimple(ListView):
    model = Event
    table_class = EventTable
    template_name = 'event_list_simple.html'


class ResultsList(SingleTableView):
    model = Result
    table_class = ResultTable
    template_name = 'event_list.html'


class PlayerList(SingleTableView):
    model = Player
    table_class = PlayerTable
    template_name = 'event_list.html'


class EventDetailView(DetailView):
    model = Event
    fields = ('g_name', 'g_date', 'g_location', 'g_tag', 'g_players', 'g_notes', 'g_winners')


def RecordList(request):
    e_data = Event.objects.all()
    w_data = Result.objects.all()
    p_data = Player.objects.all()
    g_data = Game.objects.all()
    #print(e_data)
    print(w_data)

    return render(request, 'records.html', {'e_data': e_data, 'w_data': w_data, 'p_data': p_data, 'g_data': g_data})


def DataRequest(request):
    """Shell view for retriving objects"""
    data = GetPlayers()
    print('data inside view =', data)
    return render(request, 'data.html', {'data': data})


"""
Forms - two types. 
First based on create view CLASS. Harder to pass list to template.
Second based on a view FUNCTION that calls EventForm CLASS. ALlows the function to pass list to tmaplate
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
