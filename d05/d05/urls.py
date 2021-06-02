"""d05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('ex00/', include('ex00.urls')),
    path('ex02/', include('ex02.urls')),
    path('ex03/', include('ex03.urls')),
    path('ex04/', include('ex04.urls')),
    path('ex05/', include('ex05.urls')),
    path('ex06/', include('ex06.urls')),
    path('ex07/', include('ex07.urls')),
    path('admin/', admin.site.urls),
]
