from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        first_name = 'نام خود را وارد کنید...'
        last_name = 'نام خانوادگی خود را وارد کنید...'
        email = 'ایمیل خود را وارد کنید...'
        address = 'آدرس خود را وارد کنید...'
        postal_code = 'کد پستی خود را وارد کنید...'
        city = 'نام شهر خود را وارد کنید...'
        first_name_label = 'نام'
        last_name_label = 'نام خانوادگی'
        email_label = 'ایمیل'
        address_label = 'آدرس'
        postal_code_label = 'کد پستی'
        city_label = 'شهر'

        model = Order
        fields = ['first_name', 'last_name',
                  'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': first_name}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': last_name}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': email}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': address}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': postal_code}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': city})
        }

        labels = {
            'first_name': first_name_label,
            'last_name': last_name_label,
            'email': email_label,
            'address': address_label,
            'postal_code': postal_code_label,
            'city': city_label
        }
