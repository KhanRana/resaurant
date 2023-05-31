from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Review, Menu, Table, Booking
from .forms import BookTableForm
from django.contrib.auth.decorators import login_required
from .availability import check_availability

# Create your views here.


def menu(request):
    context = {
        'menu': Menu.objects.all()
    }
    return render(request, 'bookings/menu.html', context=context)



@login_required
def booking(request):
    if request.method == 'POST':
        booking_form = BookTableForm(request.POST)
        if booking_form.is_valid():
            data = booking_form.cleaned_data
            table_list = Table.objects.filter(num=data['table'].num)
            available_tables = []
            for table in table_list:
                if check_availability(table, data['date'], data['time']):    
                    available_tables.append(table)
            
            if len(available_tables) > 0:
                new_table = available_tables[0]
                new_booking = Booking.objects.create(
                    username=request.user,
                    table=new_table,
                    date=data['date'],
                    time=data['time'],)
                new_booking.save()
                messages.success(request, 'Your table has been booked, We look forward to seeing you!')
                return redirect('gossip-menu')
            else:
                messages.error(request, 'A booking already exists, please select another table or time')
                return render(request, 'bookings/booking.html', {'booking_form': booking_form })
    else:
        booking_form = BookTableForm()
    return render(request, 'bookings/booking.html', {'booking_form': booking_form })


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5


