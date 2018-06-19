from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # ex: /api/motor/
    path('', views.index, name='index'),
    # ex: /api/motor/move?x=<x>&y=<y>&r=<r>
    path('move/', views.move, name='move'),
    # ex: /api/motor/<channel>/directdrive/<pulse>
    path('<int:channel_id>/directdrive/<int:pulse_width>/', views.directdrive, name='directdrive'),
]
