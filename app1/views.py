from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def soumya(request):
    return HttpResponse("<h1>hii, I am soumya here</h1>")

def nilesh(request):
    return render(request, 'nilesh.html')
