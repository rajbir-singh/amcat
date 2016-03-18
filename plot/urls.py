from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'plot'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^stocks/', views.ChartsView.as_view(), name='stocks'),
    url(r'^stock/chart', views.plotform , name='plotform'),
]
