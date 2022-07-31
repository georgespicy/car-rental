from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(max_length=250)

    class Meta:
        model = Brand
        fields = ('brand_name',)