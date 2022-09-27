from django.shortcuts import render
from .models import AccessLog

# Create your views here.

def introduce(request):
    user = AccessLog()
    return render(request, 'index.html')