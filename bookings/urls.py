from django.urls import path
# from .views import booking as booking_view
from .views import (booking_list,
                    BookingCreateView,
                    BookingDetailView,
                    BookingUpdateView,
                    BookingCancelView)

urlpatterns = [
    # path('bookings/',booking_view , name='gossip-booking'),
    path('user_bookings/', booking_list, name='user-bookings'),
    path('bookings/new/', BookingCreateView.as_view(), name='create-booking'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking-details'),
    path('booking/<int:pk>/update',
         BookingUpdateView.as_view(), name='booking-update'),
    path('booking/<int:pk>/delete',
         BookingCancelView.as_view(), name='booking-delete'),
]
