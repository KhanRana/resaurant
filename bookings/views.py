from django.shortcuts import render
from django.views import generic
from .models import Review, Menu
from django.contrib.auth.decorators import login_required

# Create your views here.


def menu(request):
    context = {
        'menu': Menu.objects.all()
    }
    return render(request, 'bookings/menu.html', context=context)

@login_required
def booking(request):
    return render(request, 'bookings/booking.html')

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
