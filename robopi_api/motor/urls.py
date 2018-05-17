from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # ex: /api/sensor/
    path('', views.index, name='index'),
    # ex: /api/sensor/accelerator/
    path('drive/', views.accelerator, name='drive'),
]
