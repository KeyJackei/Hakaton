# appointments/urls.py

from django.urls import path
from .views import appointment_form

urlpatterns = [
    path('', appointment_form, name='appointment_form'),
]