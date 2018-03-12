from django.conf.urls import url
from . import views

app_name = 'amcatCandidateDetails'
urlpatterns = [
    url(r'^admitCards/(?P<orderId>\d+)/(?P<count>\d+)/$', views.scrapDetails)
    # url(r'^candetails/(?P<orderId>\d+)/(?P<count>\d+)/$', views.ScrapDetails.as_view())
]
