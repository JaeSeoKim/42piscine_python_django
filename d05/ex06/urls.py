from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.Init.as_view(), name='ex06-init'),
    path('populate/', views.Populate.as_view(), name='ex06-populate'),
    path('display/', views.Display.as_view(), name='ex06-display'),
    path('remove/', views.Remove.as_view(), name='ex06-remove'),
    path('update/', views.Update.as_view(), name='ex06-update'),
]
