import django_tables2 as tables
from .models import Event, Player, Game
from django_tables2.utils import A  # alias for Accessor
from django.utils.safestring import mark_safe


class EventTable(tables.Table):
    #g_winner = tables.Column(footer="Total:")
    g_date = tables.Column(accessor='g_date', localize=True)
    id = tables.LinkColumn("event_detail", args=[A("pk")])
    g_collab = tables.Column(accessor='g_name.collab', verbose_name='Collaborative?')


    class Meta:
        model = Event
        #template_name = "django_tables2/bootstrap.html"
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("id", "g_name", "g_collab", "g_tag", "g_date", "g_location", "g_players", "g_notes", "g_winner")


class PlayerTable(tables.Table):
    event = tables.Column()

    class Meta:
        model = Player
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "name", "event")

    def render_data_from_Event(self, value, record):
        return mark_safe("</br>".join(Event.objects.filter().values_list("event", flat=True)))


