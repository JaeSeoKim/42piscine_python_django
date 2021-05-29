from django.shortcuts import render


def django(request):
    return render(request, 'ex01/django.html')


def display(request):
    return render(request, 'ex01/display.html')


def templates(request):
    return render(request, 'ex01/templates.html')
