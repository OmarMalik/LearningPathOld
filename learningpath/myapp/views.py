from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from myapp.models import Category

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.all()[:5]
    context_dict = {'categories': category_list}
    return render_to_response('myapp/index.html', context_dict, context)


def about(request):
    return render_to_response('myapp/about.html')