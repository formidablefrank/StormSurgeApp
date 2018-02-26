from django.conf.urls import url
from . import views

urlpatterns = [
    #/surgeforcast
    url(r'^$', views.index, name='index'),

	url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
	
    #/surgeforcast/message_id
    url(r'^(?P<message_id>[0-9]+)/$', views.detail, name='detail'),    

    #/surgeforcast/viewelevtimeseries/
    url(r'^viewelevtimeseries/$', views.viewElevTimeSeries, name='viewelevtimeseries'), 

    #/surgeforcast/viewelevtimeseries/timeframe
    #url(r'^viewelevtimeseries/(?P<message_id>[0-9]+)/$', views.viewElevTimeFrame, name='viewelevtimeframe'),
]