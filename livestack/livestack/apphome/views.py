from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import models

class Index(View):
    def get(self, request):
        context = {}
        return render_to_response('index.html', context)


class Download(View):
    def post(self, request):
        context = {}
        return HttpResponse("Checkout your email right now!")
