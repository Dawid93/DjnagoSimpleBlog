# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Hello<h1>")


def post_detail(request):
    return HttpResponse("<h1>Hello<h1>")


def post_list(request):
    queryset = Post.objects.all()

    context_data = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context_data)


def post_update(request):
    return HttpResponse("<h1>Hello<h1>")


def post_delete(request):
    return HttpResponse("<h1>Hello<h1>")
