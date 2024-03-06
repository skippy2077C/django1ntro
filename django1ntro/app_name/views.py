from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    return HttpResponse('<h1>Page 1</h1><a href="/page2/">oldinga</a>')

def page2(request):
    return HttpResponse('<h1>Page 2</h1><a href="/page1/">orqaga</a> <a href="/page3/">oldinga</a>')

def page3(request):
    return HttpResponse('<h1>Page 3</h1><a href="/page2/">orqaga</a> <a href="/page4/">oldinga/a>')

def page4(request):
    return HttpResponse('<h1>Page 4</h1><a href="/page3/">orqaga</a> <a href="/page5/">oldinga</a>')

def page5(request):
    return HttpResponse('<h1>Page 5</h1><a href="/page4/">Previous</a>')
