#created by me
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("welcome to about")

def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("remove punc")    

def capfirst(request):
    return HttpResponse("capfirst <a href='/'> back </a> ")     