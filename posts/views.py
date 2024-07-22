from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

