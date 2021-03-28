from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('submitted', views.submit),
    path('shows/all', views.allshows),
    path('shows/show/<int:show_id>', views.show),
    path('shows/edit/<int:show_id>', views.edit),
    path('shows/delete/<int:show_id>', views.delete),
    path('shows/editdata/<int:show_id>', views.editdata),
]