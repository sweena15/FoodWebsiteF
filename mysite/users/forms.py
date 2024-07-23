from dataclasses import fields
from django import forms
from food.models import *
from django.contrib.auth.forms import UserCreationForm
from users.models import CustCart, Profile, CustRatingFeedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2' , 'email', 'first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'user_type']


class CustCartUpd(forms.ModelForm):
    class Meta:
        model = CustCart
        # fields = ['cart_id', 'prod_code', 'quantity', 'username']
        fields = [ 'quantity']  

class CustRatFeedForm(forms.ModelForm):
    class Meta:
        model = CustRatingFeedback
        fields = ['ratings', 'feedback']