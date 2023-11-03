from django.shortcuts import render
from django.http import HttpResponse
from .models import Salute

# Create your views here.
def salute_recruiter(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить')
    salute = Salute.objects.create(name=name, message=message)
    return render(request, 'salute_template.html', {'salute': salute})