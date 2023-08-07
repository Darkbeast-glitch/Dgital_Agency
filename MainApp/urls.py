from django.urls import path
from MainApp.views import HomePage,Services,Projects,ContactUS


urlpatterns = [
    path('', HomePage , name="home"),
    path('services', Services , name="services"),
    path('projects', Projects , name="projects"),
    path('contact', ContactUS , name="contact"),
 
]
