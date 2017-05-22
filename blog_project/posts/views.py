# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Hello<h1>")


def post_detail(request):
    return HttpResponse("<h1>Hello<h1>")


def post_list(request):
    context_data = {
        "title": "List"
    }
    return render(request, "index.html", context_data)


def post_update(request):
    return HttpResponse("<h1>Hello<h1>")


def post_delete(request):
    return HttpResponse("<h1>Hello<h1>")
