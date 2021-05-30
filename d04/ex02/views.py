import logging
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from . import forms


def index(request: HttpRequest):
    logger = logging.getLogger('history')

    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['history'])
        return redirect('/ex02')
    try:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        historys = [line for line in f.readlines()]
    except:
        historys = []

    return render(request, 'ex02/index.html', {'form': forms.History(), 'historys': historys})
