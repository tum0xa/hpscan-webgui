import os
from .tools import Scanner
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hpscan/index.html')

# Create your views here.
def scan(request):
    options = request.GET.dict()
    print(options)
    scan_process = Scanner(options)
    scan_process.start()
    return HttpResponse("OK")
