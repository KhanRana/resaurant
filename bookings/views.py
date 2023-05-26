from django.shortcuts import render
from django.views import generic
from .models import Review

# Create your views here.

menu_items = [
    {
        'title': 'Memak',
        'content': 'Chicken, noodels, sprout',
        'date_created': '25/06/2023',
    },
    {
        'title':'chicken dumplings',
        'content':'Chicken, rice, wheat flour',
        'date_created':'24/06/2023',
    }
]

def menu(request):
    context = {
        'menu': menu_items
    }
    return render(request, 'bookings/menu.html', context)

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
    