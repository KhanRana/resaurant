from django.urls import path
from .views import booking as booking_view

urlpatterns = [
    path('bookings/',booking_view , name='gossip-booking'),
 
    ]