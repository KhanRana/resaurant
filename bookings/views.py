from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Review, Menu
from .forms import BookTableForm
from django.contrib.auth.decorators import login_required

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
            booking_form.save()
            messages.success(request, 'Your table has been booked, We look forward to seeing you!')
            return redirect('gossip-menu')
        
    else:
        booking_form = BookTableForm()
    return render(request, 'bookings/booking.html', {'booking_form': booking_form })


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
