from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile_create.html', {'form': form})

@login_required
def profile_view(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
