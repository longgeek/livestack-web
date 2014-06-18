#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Longgeek <longgeek@gmail.com>

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.core.mail import EmailMultiAlternatives
import models, re, threading

class Index(View):
    def get(self, request):
        context = {}
        return render_to_response('index.html', context)


class Download(View):
    def post(self, request):
        context = {}
        email = request.POST.get('email')
        recontact = re.compile(r'^[a-zA-Z0-9_]{3,18}\@[a-zA-z0-9]{2,10}\.[a-zA-Z0-9]{3,10}(\.[a-zA-Z0-9]{2,10})?$')

        who = email
        if recontact.match(email):
            sendmail('[LiveStack] Download to LiveStack ISO', [email,])
            sendmail('[LiveStack] Download to LiveStack ISO', ['livestackgroup@thstack.com',], who)
            return HttpResponse("Checkout your email right now!", context)
        else:
            return HttpResponse("Insert a valid email address!", context)


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, email):
        self.subject = subject
        self.html_content = html_content
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject,
                                     self.html_content,
                                     'LiveStack',
                                     self.email)
        msg.attach_alternative(self.html_content, "text/html")
        msg.send()


def sendmail(subject, email, who=None):
    template_path = "email.html"
    for name in email:
        context = {
            'email': name.split('@')[0]
        }

        if name.split('@')[0] == 'livestackgroup':
            context = {
                'email': name.split('@')[0],
                'emailuser': who
            }

    html_content = loader.render_to_string(template_path, context)
    emails = EmailThread(subject, html_content, email)
    emails.start()
