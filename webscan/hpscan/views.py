import os
from .tools import Scanner
from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def scan(request):
    options = request.GET.dict()
    scan_process = Scanner(options)
    scan_process.start()
    return HttpResponse("OK")