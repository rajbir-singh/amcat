from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Stock
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from . import my_attempt
# from . import charts
import sys
from . import my_attempt

class ChartsView(generic.ListView):
    template_name='plot/pickone.html'
    context_object_name='stocks_list'

    def get_queryset(self):
        return Stock.objects.all()

class Home(generic.ListView):
    template_name='plot/index.html'
    context_object_name='stocks_list'

    def get_queryset(self):
        return Stock.objects.all()

def plotform(request):

    stock = get_object_or_404(Stock, pk=request.POST['choice'])
    selected_stock = stock.lookup_symbol
    sys.stderr.write('\n*****************\n')
    sys.stderr.write(selected_stock)
    sys.stderr.write('\n*****************\n')
    return my_attempt.threadBoy(selected_stock)