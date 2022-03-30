from django.urls import path
from . import views
from . import forms


urlpatterns = [

    path('test/', views.EventFilterView, name='test'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('wins/<int:player_id>/', views.WinDataView, name='wins'),
    path('games-played/<int:player_id>/', views.PlayerDataView, name='games_played'),
    path('data/', views.DataRequest, name='data'),
    path('record/', views.RecordList, name='record'),
    path('event-list/', views.EventList.as_view()),
    path('player-list/', views.PlayerList.as_view()),
    path('event-list-simple/', views.EventListSimple.as_view()),
    path('event-form-as-view/', views.EventCreateView.as_view()),
    path('player-form-as-view/', views.PlayerCreateView.as_view()),
    path(r'event-detail-as-view/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('event-form/', views.EventFormView, name='event_form_simple'),
    path('player-form/', views.PlayerFormView, name='player_form_simple'),
    path('game-form/', views.GameFormView, name='game_form_simple'),
    path('player-data-form/', views.PlayerDataSelectFormView, name='player_data_select'),
    path('panda-winners/<int:pl>/<int:gm>/<int:op>/', views.PandasWinnerView, name='panda'),
    path('panda-results/<int:pl>/', views.PandaResultsView, name='panda-results'),
    path('chart', views.ChartView, name='chart'),
    path('chart-results/<int:pl>/<int:gm>', views.ChartResultsView, name='chart-results'),
    path('select-chart', views.SelectChart, name= 'select_chart'),
]
