from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # ex: /api/sensor/
    path('', views.index, name='index'),
    # ex: /api/sensor/accelerator/
    path('accelerator/', views.accelerator, name='accelerator'),
    # ex: /api/sensor/gyro/
    path('gyro/', views.gyro, name='gyro'),
    # ex: /api/sensor/gyro/
    path('baro/', views.baro, name='baro'),
    # ex: /polls/5/results/
    path('<int:question_id>/drive/', views.drive, name='drive'),
    # ex: /polls/5/vote/
    path('<int:question_id>/refresh/', views.refresh, name='refresh'),

]
