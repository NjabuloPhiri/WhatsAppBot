from django.urls import path
from .views import twilio_bot


urlpatterns = [
    path('', twilio_bot),
]
