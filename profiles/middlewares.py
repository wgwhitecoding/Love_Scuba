from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Check if the user has a profile
                profile = request.user.profile
            except Profile.DoesNotExist:
                # Redirect to profile creation if profile does not exist
                if request.path != reverse('profile_create'):
                    return redirect('profile_create')
        response = self.get_response(request)
        return response
