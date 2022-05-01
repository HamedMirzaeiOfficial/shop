from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'coupon', 'placeholder': 'کد تخفیف را وارد کنید ...'}))
    code.label = 'کد تخفیف'
