from django.urls import path
from api.views.views import *

urlpatterns = [
    path('register/', UserProfileListCreateView, name='register'),
]