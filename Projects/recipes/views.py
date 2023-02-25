from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("<h1>Index</h1></br><h3>principal page</h3>")


def rice(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Prepare Rice</h1>")
