from django.urls import path
from .views import marketplace_view

urlpatterns = [
    path('', marketplace_view, name='marketplace'),
]
