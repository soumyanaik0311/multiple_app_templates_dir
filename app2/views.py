from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kishore(request):
    return HttpResponse("<h1>hii, I am Kishore sir</h1>")

def harshad(request):
    return render(request, 'harshad.html')
