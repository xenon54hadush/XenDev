from django import forms
from .models import AdminBoard
from myapp.models import Project


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminBoard
        fields = ['title', 'body', 'image']

        labels = {
            'title': 'Title',
            'body': 'Body',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title', 'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Post Content.....', 'class': 'form-control'
            }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']

        labels = {
            'title': 'Project title',
            'description': 'Description',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Project title', 'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Short description of the project', 'class': 'form-control', 'rows': 4
            }),
        }
