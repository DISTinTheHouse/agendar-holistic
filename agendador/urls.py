from django.urls import path
from .views import agendar_cita, webhook_cal, dashboard_citas

urlpatterns = [
    path('', agendar_cita, name='agendar_cita'),
    path('webhook/cal/', webhook_cal, name='webhook_cal'),
    path('dashboard/', dashboard_citas, name='dashboard_citas'),
]
