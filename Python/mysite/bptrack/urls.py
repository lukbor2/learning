from django.conf.urls import url
from django.conf import settings
from bptrack import views
from bptrack.views import PatientList, PatientDetail, PatientBPMeasure

app_name = 'bptrack'

urlpatterns = [
               
    #url(r'^search-form/$', views.search_form),
    url(r'^home/$', PatientList.as_view()),
    url(r'^patient_detail/(?P<pk>[0-9]+)$', PatientDetail.as_view()),
    url(r'^patient_bpmeasure/([0-9]+)$', PatientBPMeasure.as_view()),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
