from django.shortcuts import render
from .models import DiveLocation

def travel_view(request):
    locations = DiveLocation.objects.all()
    return render(request, 'travel/travel.html', {'locations': locations})

