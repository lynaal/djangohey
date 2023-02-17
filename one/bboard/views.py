from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Bb
from .models import Rubric

def by_rubric (request, rubric_id):
    bbs=Bb.object.filter(rubric=rubric_id)
    rubrics=Rubric.object.all
    current_rubric=Rubric.object.get(pk=rubric_id)
    context={'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
    #
    # s = 'Cписок объявлений\г\п\г\п\г\п'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
