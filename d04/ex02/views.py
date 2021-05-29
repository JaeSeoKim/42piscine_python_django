import logging
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from . import forms

logger = logging.getLogger('history')


def index(request: HttpRequest):
    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['history'])
            return redirect('history')
        else:
            return redirect('')
    else:
        return render(request, 'ex02/index.html', {'form': forms.History()})


def history(request: HttpRequest):
    try:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        historys = [line for line in f.readlines()]
        return render(request, 'ex02/history.html', {'historys': historys})
    except:
        return render(request, 'ex02/history.html', {'historys': []})
