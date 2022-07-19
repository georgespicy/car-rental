from django import forms
from .models import Contact

class formcontact(forms.ModelForm):
    Fullname = forms.CharField(max_length=100)
    Email = forms.EmailField(label="Email")
    Subject = forms.CharField(max_length=100)
    Message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ('Fullname', 'Email', 'Subject', 'Message')