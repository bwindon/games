from django.urls import path
from . import views
from . import forms


urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('player-data-totals/', views.PlayerDataTotalsView, name='player-data-totals'),
    path('event-list/', views.EventList.as_view()),
    path('player-list/', views.PlayerList.as_view()),
    path('event-list-simple/', views.EventListSimple.as_view()),
    path('event-form-as-view/', views.EventCreateView.as_view()),
    path('player-form-as-view/', views.PlayerCreateView.as_view()),
    path(r'event-detail-as-view/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('event-form/', views.EventFormView, name='event_form_simple'),
    path('player-form/', views.PlayerFormView, name='player_form_simple'),
    path('game-form/', views.GameFormView, name='game_form_simple'),
    path('panda-winners/<int:pl>/<int:gm>/<int:op>/', views.PandasWinnerView, name='panda'),
    path('panda-results/<int:pl>/', views.PandaResultsView, name='panda-results'),
    path('chart', views.ChartView, name='chart'),
    path('chart-results/<int:pl>/<int:gm>', views.ChartResultsView, name='chart-results'),
    path('select-chart', views.SelectChart, name= 'select_chart'),
    path('google/<int:pl>/<int:gm>', views.GoogleChartResultsView, name='google-chart'),
    path('google-dashboard/<int:pl>/<int:gm>', views.GoogleDashboardView, name='google-dashboard'),
    path('dataframe-dashboard/<int:pl>', views.DataframeDashboardView, name='dataframe-dashboard'),
    path('dataframe-dashboard-stacked/<int:pl>', views.DataframeDashboardStackedView, name='dataframe-dashboard-stacked'),
    path('dataframe-list/<int:pl>', views.DataFrameToListView, name='dataframe-list'),
]
