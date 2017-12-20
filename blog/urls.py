from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$',blog.views.archive),
    url(r'^create/',blog.views.create_blogpost),
]