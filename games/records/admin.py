from django.contrib import admin
from .models import Game, Player, Event, Result
# Register your models here.

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Result)
