from django import db
from django.views import View
from django.shortcuts import render
from ..forms import TipForm, DeleteTipForm
from ..models import TipModel


class Index(View):
    template_name = "index.html"

    def get(self, request):
        try:
            tips = TipModel.objects.all().order_by('-date')
        except db.DatabaseError as e:
            tips = []
        context = {
            'tipform': TipForm(),
            'tips': [{
                'id': tip.id,
                'content': tip.content,
                'author': tip.author,
                'date': tip.date,
                'deleteform': DeleteTipForm(tip.id),
            } for tip in tips],
        }
        return render(request, self.template_name, context)
