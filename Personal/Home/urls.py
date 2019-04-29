import os
import sys

from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500

from . import views 

HOME_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(HOME_DIR)
PERSONAL_DIR = os.path.join(BASE_DIR, 'Personal')
sys.path.append(PERSONAL_DIR)

from Personal import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('update_access_logs', views.update_access_logs, name="update_access_logs"),
    path('update_access_logs/triggered', views.update_access_logs_triggered, name="update_access_logs_triggered"),
    path('about_me/', views.about_me, name="about_me"),
    path('about_me/download_resume', views.download_resume, name="download_resume"),
    path('connect/', views.connect, name="connect"), 
    path('connect/thanks_for_reaching_out/', views.connect, name="thank_you"),
    path('projects/', views.projects, name="projects_home_page"),
    path('projects/random_word_generator', views.random_word_generator, name="random_word_generator"),
    path('projects/random_word_generator_ajax', views.random_word_generator_ajax, name="random_word_generator_ajax"),
    path('projects/random_name_generator', views.random_name_generator, name="random_name_generator"),
    path('projects/upload_pdf', views.upload_pdf, name="upload_pdf"), 
    path('projects/display_content', views.display_content, name="display_content"),
    path('projects/reaction_time_test', views.reaction_time_test, name="reaction_time_test"),
    path('projects/linkedin_bot', views.linkedin_bot, name="linkedin_bot"),
    path('projects/access_log_visualizer', views.access_log_visualizer, name="access_log_visualizer"),
    path('test/500', views.test_500, name="500_test"),
]




