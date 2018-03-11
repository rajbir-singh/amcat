import sys
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from amcatCandidateDetails import crawlCandidateDetails
from . import executor as exc
import os

def scrapDetails(self, orderId, count):
    sys.stderr.write('\n*****************\n')
    sys.stderr.write(orderId + ', ' + count)
    sys.stderr.write('\n*****************\n')
    fileName = crawlCandidateDetails.pullDetails(orderId, count)
    # return  crawlCandidateDetails.download_file(fileName)
    template_name='candetails.html'
    count = 0
    orderId = 0
    # ork = exc.execute("sudo pip install pandas", os.getcwd())
    # context = {'output' : ork[0], 'errors' : ork[1]}
    context = {'output': fileName}
    return render(self, 'candetails.html', context)

    # def get_queryset(self):
     #    orderId = self.kwargs['orderId']
     #    count = self.kwargs['count']
    # fileName = crawlCandidateDetails.pullDetails(orderId, count)
    # return  crawlCandidateDetails.download_file(fileName)
    # output, errors = exc.execute("sudo pip install pandas", os.getcwd())
	# return render_to_response('candetails.html', console_gave = [output, errors])

class ScrapDetails(generic.ListView):
    # template_name='candetails.html'
    # count = 0
    # orderId = 0
    # def get_queryset(self):
     #    orderId = self.kwargs['orderId']
     #    count = self.kwargs['count']
    # # fileName = crawlCandidateDetails.pullDetails(orderId, count)
    # # return  crawlCandidateDetails.download_file(fileName)
    # output, errors = exc.execute("sudo pip install pandas", "/home/user/")
	# return render_to_response('homepage.html', console_gave = [output, errors])
    def get_queryset(self):
        return ""