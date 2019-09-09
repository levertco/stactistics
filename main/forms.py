from django import forms
from .models import Review,Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model= Website
        exclude= ['reviews','owner']

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields='__all__'