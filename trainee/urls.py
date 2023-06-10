from django.urls import path
from .views import *

urlpatterns = [
     path('', Tlist, name='Traineelist'),
    path('update/<int:ID>', TUpdate, name='Traineeupdate'),
    path('delete/<int:ID>', TDelete, name='Traineedelete'),
    path('add', Tadd, name='TraineeAdd'),
]
