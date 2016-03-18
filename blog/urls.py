from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.views.generic import ListView, DeleteView
from blog.models import Blog

app_name = 'blog'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'blog_home$', ListView.as_view(queryset=Blog.objects.all().order_by('-pub_date')[:25], template_name='blog/blog.html'), name='blogs'),
    url(r'^debug$', ListView.as_view(queryset=Blog.objects.all(), template_name='blog/sdownproto.html')),
    url(r'form/$', views.get_post, name='first_form'),
    url(r'create/$', views.new_post, name='new_form'),
]
