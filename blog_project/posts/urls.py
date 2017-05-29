from django.conf.urls import url
from django.contrib import admin


from .views import (
    post_list,
    post_detail,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]
