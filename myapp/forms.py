from django import forms
from .models import Client
from phonenumber_field.modelfields import PhoneNumberField

class ClientForms(forms.ModelForm):
    phone_number = PhoneNumberField(region= 'ET')
    class Meta:
        model = Client
        fields = ['title','firstname', 'lastname', 'phone_number', 'email', 'contents']

        lables = {
            'title': 'Title',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'contents': 'Contents',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title', 'class': 'form-control'
            }),
            'firstname': forms.TextInput(attrs={
                'placeholder': 'First Name', 'class': 'form-control'
            }),
            'lastname': forms.TextInput(attrs={
                'placeholder': 'Last Name', 'class': 'form-control'
            }),
            'phone_number': forms.NumberInput(attrs={
                'placeholder': '+251 9....', 'class':'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email', 'class': 'form-control'
            }),
            'contents': forms.Textarea(attrs={
                'placeholder': 'Description ......', 'class': 'form-control'
            })
        }