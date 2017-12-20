# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render_to_response
from blog.models import BlogPost,BlogPostForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()[:10]
    c = {'posts': posts,'form':BlogPostForm()}
    c.update(csrf(request))
    return render_to_response('archive.html',c)


def create_blogpost(request):
    if request.method =='POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
        return HttpResponseRedirect('/blog/')

