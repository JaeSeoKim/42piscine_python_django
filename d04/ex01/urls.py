from django.urls import path

from . import views

urlpatterns = [
    path('django', views.django, name='django'),
    path('display', views.display, name='display'),
    path('templates', views.templates, name='templates'),
]
