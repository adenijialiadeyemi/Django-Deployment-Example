from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html')


def other(request):
    return render(request, 'basic_app/other.html')


def rel_temp(request):
    return render(request, 'basic_app/rel_temp.html')

