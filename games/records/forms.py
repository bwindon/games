from django import forms
from .models import Event, Player, Game
from django.forms.widgets import NumberInput, Textarea, TextInput, Select
"""
PLAYER_CHOICES = (
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)
GAME_CHOICES = (
    ('#1', 'Transaction'),
    ('#2', 'Sales Date'),
    ('#3', 'Customer ID'),
    ('#4', 'Total Price')
)

CHART_CHOICES = (
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)
"""
"""
class PlayerDataSelectForm(forms.Form):
    player = forms.ChoiceField(choices=PLAYER_CHOICES)
    game = forms.ChoiceField(choices=GAME_CHOICES)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
"""

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


class PlayerDataSelectForm(forms.Form):


    class Meta:
        #model = Game
        fields = ('name', 'game', 'chart')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the query here
        MYQUERY = Player.objects.values_list('id', 'name')
        self.fields['name'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(*MYQUERY,))
        MYQUERY2 = Game.objects.values_list('id', 'name')
        self.fields['game'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(*MYQUERY2,))

        CHART_CHOICES = (
            ('1', 'Bar Graph'),
            ('2', 'Pie Chart'),
            ('3', 'Line Graph')
        )
        self.fields['chart'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(*CHART_CHOICES,))

