from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "Recipes/home.html", context={
        "message": "Hello, Welcome Pagine Home"
    })


def rice(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Prepare Rice</h1>")
