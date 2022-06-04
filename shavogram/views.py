from django.shortcuts import render,redirect
from .models import Photo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    images = Photo.objects.all()
    return render(request,"index.html", {"images":images})

