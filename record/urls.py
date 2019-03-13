from django.conf.urls import include, url
from django.contrib import admin
from .views import SpecialistList,RecordingView


urlpatterns = [
    url(r'^$', SpecialistList.as_view(), name='start'),
    url(r'^doctor/(?P<specialist_id>\d+)/$',RecordingView.as_view(), name='recording'),

]
