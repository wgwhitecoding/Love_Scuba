from django.urls import path
from .views import profile_create, profile_view

urlpatterns = [
    path('create/', profile_create, name='profile_create'),
    path('<str:username>/', profile_view, name='profile'),
]

