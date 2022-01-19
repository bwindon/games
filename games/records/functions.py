from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event, Result, Player, Game
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import EventTable, ResultTable,PlayerTable


def GetPlayers():
    """Get players in events"""
    data = list(Player.objects.values_list('name', flat=True))
    #data = Player.objects.all
    return data

