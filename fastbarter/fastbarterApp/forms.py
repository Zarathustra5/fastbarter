from django import forms
from .models import *
from users.models import *

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'city', 'phone_number', 'email', 'photo')

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('photo', 'title', 'short_desc', 'price', 'category', 'category_exchange')
        widgets = {
            'short_desc': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('catalog', 'user')