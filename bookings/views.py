from django.shortcuts import render
from django.views import generic
from .models import Review, Menu

# Create your views here.


def menu(request):
    context = {
        'menu': Menu.objects.all()
    }
    return render(request, 'bookings/menu.html', context=context)


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
