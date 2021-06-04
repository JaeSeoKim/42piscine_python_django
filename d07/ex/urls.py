from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('articles/<slug:pk>/', views.Detail.as_view(), name='articles_detail'),
    path('publish/', views.Publish.as_view(), name='publish'),
    path('publications/', views.Publications.as_view(), name='publications')

]
