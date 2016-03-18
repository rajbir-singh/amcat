from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Blog
from .forms import postBlog
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from . import my_attempt
# from . import charts
import sys

class Entries(generic.ListView):
    template_name='blog/blog.html'
    context_object_name='blogs_list'

    def get_queryset(self):
        return Blog.objects.all()


def get_post(request):

    #Method  = POST
    if request.method == 'POST':
        form = postBlog(request.POST)
        if form.is_valid():
            # sys.stderr.write(form.cleaned_data['name'])

            """     ***     UPDATE DATABASE HERE        ***     """

            return HttpResponseRedirect('blog.html')

        else:
            sys.stderr.write('$$$$$$$$$')
    else:
    #Method =  GET

        form = postBlog()
    return render(request, 'blog/name.html', {'form' : form})


def new_post(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        data = request.POST['data']
        Blog.objects.create(
            name = name,
            email = email,
            title = title,
            data = data
        )

        return HttpResponse('')

# class Home(generic.ListView):
#     template_name='plot/index.html'
#     context_object_name='stocks_list'
#
#     def get_queryset(self):
#         return Stock.objects.all()
#
# def plotform(request):
#
#     stock = get_object_or_404(Stock, pk=request.POST['choice'])
#     selected_stock = stock.lookup_symbol
#     sys.stderr.write('\n*****************\n')
#     sys.stderr.write(selected_stock)
#     sys.stderr.write('\n*****************\n')
#     return my_attempt.threadBoy(selected_stock)