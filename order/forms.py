from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید...'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس خود را وارد کنید...'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی خود را وارد کنید...'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شهر خود را وارد کنید...'})
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'address': 'آدرس',
            'postal_code': 'کد پستی',
            'city': 'شهر'
        }
