# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)

    context_data = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "portfolio-page.html", context_data)


def post_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 12)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context_data = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "portfolio.html", context_data)
