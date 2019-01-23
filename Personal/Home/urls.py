from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500

from . import views 

urlpatterns = [
    path('', views.home, name="home"),
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
    path('test/404', views.test_404, name="404_test"),
]


# handler404 = 'Home.views.error_404'
# handler500 = 'Home.views.error_500'



