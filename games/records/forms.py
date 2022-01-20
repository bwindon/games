from django import forms
from .models import Event, Player, Game
from django.forms.widgets import NumberInput, Textarea, TextInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('g_name', 'g_location', 'g_date', 'g_tag', 'g_players', 'g_winner', 'g_notes')

        widgets = {
            'g_date': NumberInput(attrs={'type': 'date'}),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'add new player'})

        }


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'add new game'})

        }
