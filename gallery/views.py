from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.

def home(request):
    images = Image.get_all_images()
    locations = Location.objects.all()

    context ={
        "images":images,
        "locations":locations
    }

    return render(request,'gallery/home.html',context)

def search(request):

    if 'category' in request.GET and request.GET["category"]:
        query = request.GET.get("category")
        res = Image.search_by_category(query)
        message = f'{query}'

        context = {
            'images': res,
            "message":message
        }

        
        
        return render(request,'gallery/search.html',context)

    else:
        message = 'You have not searched for any item'
        return render(request,'gallery/search.html',message)
def filter_location(request):
    if 'location' in request.GET and request.GET["location"]:
        query = request.GET.get("location")
        res = Image.filter_by_location(query)
        message = f'{query}'

        context = {
            'images': res,
            "message":message
        }

        
        
        return render(request,'gallery/location.html',context)

    else:
        return render(request,'gallery/location.html',context)

   

