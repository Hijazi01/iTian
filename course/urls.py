from django.urls import path
from .views import *

urlpatterns = [
     path('', Clist, name='courselist'),
     path('add', Cadd, name='courseadd'),
     path('delete/<int:ID>', Cdelete, name='coursedelete'),
     path('update/<int:id>', Cupdate, name='courseupdate'),

 ]
