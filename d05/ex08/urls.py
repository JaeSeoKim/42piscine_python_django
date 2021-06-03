from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.Init.as_view(), name='ex08-init'),
    path('populate/', views.Populate.as_view(), name='ex08-populate'),
    path('display/', views.Display.as_view(), name='ex08-display'),
]
