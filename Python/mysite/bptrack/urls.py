from django.conf.urls import url
from django.conf import settings
from . import views
# from bptrack.views import PatientList, PatientDetail, PatientBPMeasure, PatientCreate

app_name = 'bptrack'

urlpatterns = [
    #url(r'^search-form/$', views.search_form),
    url(r'^home/$', views.PatientListSearch.as_view(), name = 'patient-list'),
    url(r'^patient_detail/(?P<pk>[0-9]+)$', views.PatientDetail.as_view(), name = 'patient-detail'),
    url(r'^patient_bpmeasure/([0-9]+)$', views.PatientBPMeasure.as_view()),
    url(r'^patient_add/$', views.PatientCreate.as_view(), name = 'patient-add'),
    url(r'^patient_delete/(?P<pk>[0-9]+)$', views.PatientDelete.as_view(), name = 'patient-delete'),
    url(r'^patient_update/(?P<pk>[0-9]+)$', views.PatientUpdate.as_view(), name = 'patient-update'),
    url(r'^patient_add2/$', views.PatientCreate_v2.as_view(), name = 'patient-add2'),
    url(r'^old_home/$', views.PatientList.as_view(), name = 'patient-list-old'),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
