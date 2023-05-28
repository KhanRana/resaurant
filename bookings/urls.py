from django.urls import path
from .views import booking as booking_view

urlpatterns = [
    path('booking/', booking_view, name='gossip-booking'),
    ]