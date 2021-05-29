from django.shortcuts import render


def index(request):
    step = 255 / 50
    context = {
        "range": [
            "{:02X}".format(255 - int(i * step)) for i in range(50)
        ]
    }
    return render(request, 'ex03/index.html', context)
