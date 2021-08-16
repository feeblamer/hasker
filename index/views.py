from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    title = 'HASKER'
    context = {'site_name':title}
    return render(request, 'index/index.html', context)
