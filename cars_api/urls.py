#Author: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

from django.urls import path
from .views import CarView

urlpatterns = [
    path('', CarView.as_view(),name='cars'),
    path('<int:id>', CarView.as_view(),name='car_id'),
]

