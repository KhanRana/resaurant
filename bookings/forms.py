from django import forms
from .models import Booking, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body',)

 

