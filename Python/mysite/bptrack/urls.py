from django.conf.urls import url
from django.conf import settings
from bptrack import views
from bptrack.views import PatientList, PatientDetail, PatientBPMeasure, PatientCreate

app_name = 'bptrack'

urlpatterns = [
               
    #url(r'^search-form/$', views.search_form),
    url(r'^home/$', PatientList.as_view()),
    url(r'^patient_detail/(?P<pk>[0-9]+)$', PatientDetail.as_view(), name = 'patient-detail'),
    url(r'^patient_bpmeasure/([0-9]+)$', PatientBPMeasure.as_view()),
    url(r'^patient_add/$', PatientCreate.as_view(), name = 'patient-create'),

]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
