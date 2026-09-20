from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='myfit-home'),
    path('accounts/', include('django.contrib.auth.urls')), # This is to include the default views available for authenticating users.
]
