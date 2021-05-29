from django import forms
from .models import Document,pdfDocument
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form_record_name'}),
            'summary': forms.Textarea(attrs={'class': 'form_record_sum'}),
            'img': forms.FileInput(attrs={'class': 'form_record_img'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form_record_doc'}),
        }
        exclude = ('duser',)

class pdfform(forms.ModelForm):
    class Meta:
        model = pdfDocument

        fields = ('__all__')