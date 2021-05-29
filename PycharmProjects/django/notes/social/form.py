from .models import posts
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class editpost(forms.ModelForm):
    sid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, max_length=20)
    sname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, max_length=100)
    sage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, max_length=5)
    saddress = forms.CharField(max_length=15)

    class Meta:
        model = posts
        fields = "__all__"