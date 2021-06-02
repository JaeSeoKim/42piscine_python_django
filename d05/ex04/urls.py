from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.Init.as_view(), name='ex04-init'),
    path('populate/', views.Populate.as_view(), name='ex04-populate'),
    path('display/', views.Display.as_view(), name='ex04-display'),
    path('remove/', views.Remove.as_view(), name='ex04-remove'),
]
