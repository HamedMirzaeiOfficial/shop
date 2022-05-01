from django import forms
from django.core.exceptions import ValidationError

from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید...'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام خود را وارد کنید...'})
        }
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'message': 'پیام',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام خود را وارد کنید...'})
        }

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'hamed mirzaei':
            raise ValidationError("Sorry, you cannot use this name.")
        return data


