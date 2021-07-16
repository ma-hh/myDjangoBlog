from django.shortcuts import render
from django.shortcuts import HttpResponse

def about (request):
    #return HttpResponse("Hello its about page!")
     return render(request, 'about.html')
def home (request):
    #return HttpResponse("Its HomePage, Welcome!")
    return render (request, 'home.html')

def asl (request):
    return HttpResponse('mohammad 20 tehran')
