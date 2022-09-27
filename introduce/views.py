from django.shortcuts import render
''' 절대경로 사용'''
from introduce.models import AccessLog

# Create your views here.

def introduce(request):
    # case1
    
    '''
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()
    '''

    # case2
    AccessLog.objects.create(
        location="introduce"
    )

    return render(request, 'introduce.html')