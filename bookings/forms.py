from django import forms
from .models import Booking, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body',)


class DateInput(forms.DateInput):
    """Create date widget for the form field"""
    input_type = 'date'

class BookingForm(forms.ModelForm):
    """Booking form to get user input for the booking"""
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time']
        widgets = {
            'date': DateInput(),
        }