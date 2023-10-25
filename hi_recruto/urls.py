from django.urls import path
from .views import salute_recruiter


urlpatterns = [
    path('', salute_recruiter, name='salute_recruiter'),
]
    