from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'page_date', 'picture']
        widgets = {
            'page_date': forms.DateInput(attrs={'type': 'date'}),
        }
