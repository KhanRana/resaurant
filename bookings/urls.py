from django.urls import path
# from .views import booking as booking_view
from .views import booking_list, CreateBookingView

urlpatterns = [
    # path('bookings/',booking_view , name='gossip-booking'),
    path('user_bookings/',booking_list, name='user-bookings'),
    path('bookings/new/', CreateBookingView.as_view(), name='create-booking')

    ]