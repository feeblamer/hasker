from django.shortcuts import render
from django.http import HttpResponse
from index.services import get_all_questions

def index(request):
    title = 'HASKER'
    all_questions = get_all_questions()
    context = {'site_name':title, 'all_questions':all_questions}
    return render(request, 'index/index.html', context)
