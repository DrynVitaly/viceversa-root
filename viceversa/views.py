from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


def home (reqvest):
    return render(reqvest, 'home.html')


