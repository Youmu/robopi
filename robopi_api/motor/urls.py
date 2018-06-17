from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # ex: /api/motor/
    path('', views.index, name='index'),
    # ex: /api/motor/<channel>/drive/<pulse>
    path('<int:channel_id>/drive/<int:pulse_width>/', views.drive, name='drive'),
]
