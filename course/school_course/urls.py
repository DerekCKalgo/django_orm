from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('delete/<int:course_id>', views.delete),
    path('deletethis/<int:course_id>', views.deletethis),
]