from django.conf.urls import url
from django.conf import settings
from . import views
# from bptrack.views import PatientList, PatientDetail, PatientBPMeasure, PatientCreate

app_name = 'bptrack'

urlpatterns = [
    #url(r'^search-form/$', views.search_form),
    url(r'^home/$', views.PatientList.as_view(), name = 'patient-list'),
    url(r'^patient_detail/(?P<pk>[0-9]+)$', views.PatientDetail.as_view(), name = 'patient-detail'),
    url(r'^patient_bpmeasure/([0-9]+)$', views.PatientBPMeasure.as_view()),
    url(r'^patient_add/$', views.PatientCreate.as_view(), name = 'patient-add'),
    url(r'^patient_delete/(?P<pk>[0-9]+)$', views.PatientDelete.as_view(), name = 'patient-delete'),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
