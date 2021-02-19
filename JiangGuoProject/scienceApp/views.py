from django.shortcuts import render
from django.shortcuts import HttpResponse


def science(request):
    return render(request, 'science.html')
