from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_dojo', views.dojos),
    path('create_ninj', views.ninj)
]