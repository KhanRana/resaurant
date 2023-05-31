from datetime import date, time
from .models import Table, Booking

def check_availability(table, booking_date, booking_time):
    available_list = []
    booked_list = Booking.objects.filter(table=table)
    for booking in booked_list:
        if ((booking.time == booking_time) and (booking.date == booking_date)):
            available_list.append(False)
        else:
            available_list.append(True)
    return all(available_list)

