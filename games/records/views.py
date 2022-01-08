from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import EventTable
# Create your views here.


def menu(request):
    return HttpResponse("This is the beginning of a menu page")


class EventList(SingleTableView):
    model = Event
    table_class = EventTable
    template_name = 'event_list.html'


class EventListSimple(ListView):
    model = Event
    table_class = EventTable
    template_name = 'event_list_simple.html'
