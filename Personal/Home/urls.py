from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('resume/', views.resume, name="resume"),
    path('about_me/', views.about_me, name="about_me"),
    path('connect/', views.connect, name="connect"), 
]
