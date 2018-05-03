from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.status, name='status'),
    # ex: /polls/5/results/
    path('<int:question_id>/drive/', views.drive, name='drive'),
    # ex: /polls/5/vote/
    path('<int:question_id>/refresh/', views.refresh, name='refresh'),

]
