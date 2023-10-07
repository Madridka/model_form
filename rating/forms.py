from django import forms
from .models import *


class AddRating(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['name', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'})
        }
