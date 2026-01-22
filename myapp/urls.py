from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    # compatibility route
    path("mysection/", views.mysection, name="mysection"),
    path("download-resume/", views.download_resume, name="download_resume"),
]