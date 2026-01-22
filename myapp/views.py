from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import FileResponse
from django.conf import settings
import os


def home(request):
    # Landing / home page
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html", {"projects": projects})



def resume(request):
    return render(request, "resume.html")


# keep compatibility name for previous route
def mysection(request):
    return redirect("home")


def download_resume(request):
    file_path = os.path.join(settings.STATIC_ROOT, "resume", "Sooraj_A_Resume.pdf")
    return FileResponse(open(file_path, "rb"), as_attachment=True, filename="Sooraj_A_Resume.pdf")