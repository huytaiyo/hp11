from django import forms
from django.contrib.auth.models import User 
from .models import Order
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= ['customer_name','phone','address','payment_method']
        labels = {
            'customer_name': 'Họ và tên',
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ',
            'payment_method': 'Phương thức thanh toán',
        }      
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }