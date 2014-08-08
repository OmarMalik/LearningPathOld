from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "the message"}
    # return HttpResponse("hello");
    return render_to_response('myapp/index.html', context_dict, context)


def about(request):
    return render_to_response('myapp/about.html')