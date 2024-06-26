from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def greeshma(request):
    return HttpResponse("<h1>hii, I am greeshma ma'am here</h1>")

def jyotshna(request):
    return render(request, 'jyotshna.html')
