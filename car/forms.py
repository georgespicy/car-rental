from django import forms
from .models import Brand, Booking

class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(max_length=250)

    class Meta:
        model = Brand
        fields = ('brand_name',)

class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = ('city', 'to_state', 'To_agree')