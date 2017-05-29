# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/" % (instance.id, filename)


class Series(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name_plural = "Series"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/series/%s" % self.slug


class Post(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to=None, null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    series = models.ForeignKey(Series, related_name='post_category', null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp"]


# class SeriesToPost(models.Model):
#     post = models.ForeignKey(Post)
#     series = models.ForeignKey(Series)
