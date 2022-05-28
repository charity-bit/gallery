from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.

def home(request):
    images = Image.get_all_images()

    context ={
        "images":images
    }

    return render(request,'gallery/home.html',context)
