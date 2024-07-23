from django import forms
from food.models import *
from django.contrib.auth.forms import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['rest_owner', 'prod_code', 'item_name', 'item_desc', 'item_price', 'item_image']