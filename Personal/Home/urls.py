from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about_me/', views.about_me, name="about_me"),
    path('connect/', views.connect, name="connect"), 
    path('connect/thanks_for_reaching_out/', views.connect, name="thank_you"),
    path('projects/', views.projects, name="projects_home_page"),
    path('projects/random_word_generator', views.random_word_generator, name="random_word_generator"),
    path('projects/random_word_generator_ajax', views.random_word_generator_ajax, name="random_word_generator_ajax"),
]
