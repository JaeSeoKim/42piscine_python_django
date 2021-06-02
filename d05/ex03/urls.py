from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.populate, name='ex03-populate'),
    path('display/', views.display, name='ex03-display'),
]
