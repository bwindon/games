from django.urls import path
from . import views
from . import forms


urlpatterns = [

    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('wins/<int:player_id>/', views.WinDataView, name='wins'),

    path('data/', views.DataRequest, name='data'),
    path('record/', views.RecordList, name='record'),

    path("event-list/", views.EventList.as_view()),
    path("player-list/", views.PlayerList.as_view()),
    path('event-list-simple/', views.EventListSimple.as_view()),


    path('event-form-as-view/', views.EventCreateView.as_view()),
    path('player-form-as-view/', views.PlayerCreateView.as_view()),
    path(r'event-detail-as-view/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),


    path('event-form/', views.EventFormView, name='event_form_simple'),
    path('player-form/', views.PlayerFormView, name='player_form_simple'),
    path('game-form/', views.GameFormView, name='game_form_simple'),

]
