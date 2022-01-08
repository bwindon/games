import django_tables2 as tables
from .models import Event


class EventTable(tables.Table):
    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap.html"
        #template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("id", "g_name", "g_tag", "g_date", "g_location", "g_players", "g_notes", "g_winner")
