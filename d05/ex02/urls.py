from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init, name='ex02-init'),
    path('populate/', views.populate, name='ex02-populate'),
    path('display/', views.display, name='ex02-display'),
]
