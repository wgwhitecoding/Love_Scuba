from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item

@login_required
def marketplace_view(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'marketplace/marketplace.html', {'items': items})

