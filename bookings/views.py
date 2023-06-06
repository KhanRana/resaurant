from django import forms
from .forms import BookingForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin,)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (ListView, 
CreateView,
DetailView,
UpdateView,
DeleteView,
)
from .models import Review, Menu, Table, Booking
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .availability import check_availability


# Create your views here.


class BookingCreateView(LoginRequiredMixin, CreateView, forms.ModelForm):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(num=data['table'].num)
        available_tables = []
        for table in table_list:
            if check_availability(table, data['date'], data['time']):    
                 available_tables.append(table)
            
        if len(available_tables) > 0:
            new_table = available_tables[0]
            new_booking = Booking.objects.create(
                username=self.request.user,
                table=new_table,
                date=data['date'],
                time=data['time'],)
            new_booking.save()
            messages.success(self.request, '''Your table has been booked! 
                             Please look at our delicious menu and pick your favourites. 
                             We look forward to seeing you!''')
            return redirect('gossip-menu')
        else:
            messages.error(self.request,'''A booking already exists,
              please select another table or time''')
            return redirect('create-booking')

class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(num=data['table'].num)
        available_tables = []
        for table in table_list:
            if check_availability(table, data['date'], data['time']):    
                 available_tables.append(table)
            
        if len(available_tables) > 0:
            new_table = available_tables[0]
            new_booking = Booking.objects.create(
                username=self.request.user,
                table=new_table,
                date=data['date'],
                time=data['time'],)
            new_booking.save()
            messages.success(self.request, '''Your table has been booked! 
                             Please look at our delicious menu and pick your favourites. 
                             We look forward to seeing you!''')
            return redirect('gossip-menu')
        else:
            messages.error(self.request,'''A booking already exists,
              please select another table or time''')
            return HttpResponseRedirect(self.request.path_info)
    
    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.username:
            return True
        else:
            return False

class BookingCancelView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """Menu view as a list and dislplay the list by lower to higher price"""
    model = Booking
    success_url = '/'
    success_message = 'Your booking has been cancelled successfully!'
    
    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.username:
            return True
        else:
            return False

class MenuListView(ListView):
    """Menu view as a list and dislplay the list by lower to higher price"""
    model = Menu
    template_name = 'bookings/menu.html'
    context_object_name = 'menu'
    ordering = ['price']    


@login_required
def booking_list(request):
    if (request.user.is_authenticated):
        context = {'user_bookings': Booking.objects.filter(username=request.user)}
        return render(request, 'bookings/user_bookings.html', context=context)
    else:
        messages.error(request, "You need to login to view this page!")
        return redirect('gossip-login')


class BookingDetailView(DetailView):
    """Details of a booking in a separate view"""
    model = Booking


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(approved=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 1


