import django_tables2 as tables
from .models import Event, Player
from django_tables2.utils import A  # alias for Accessor


class EventTable(tables.Table):
    g_winner = tables.Column(footer="Total:")
    g_date = tables.Column(accessor='g_date', localize=True)
    id = tables.LinkColumn("event_detail", args=[A("pk")])

    class Meta:
        model = Event
        #template_name = "django_tables2/bootstrap.html"
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("id", "g_name", "g_tag", "g_date", "g_location", "g_players", "g_notes", "g_winner")


class PlayerTable(tables.Table):
    class Meta:
        model = Player
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "name")
