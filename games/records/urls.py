from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path("event-list/", views.EventList.as_view()),
    path('event-list-simple/', views.EventListSimple.as_view()),
]
