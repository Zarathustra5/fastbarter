from django import forms
from .models import *
from users.models import *

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'city', 'phone_number', 'email', 'photo')
        widgets = {
            'short_desc': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('photo', 'title', 'short_desc', 'price', 'category', 'category_exchange')
        widgets = {
            'short_desc': forms.Textarea(attrs={'cols': 88, 'rows': 10})
        }

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('catalog', 'user')

class FilterForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('price', 'category')

class NewChatForm(forms.ModelForm):
    class Meta:
        model = Chats
        fields = ('user1', 'user2', 'catalog')

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('user', 'text', 'chat')

class NewGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('photo', 'title', 'short_desc')
        widgets = {
            'short_desc': forms.Textarea(attrs={'cols': 88, 'rows': 10})
        }

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review', 'file', 'rating', 'catalog', 'user')
        widgets = {
            'review': forms.Textarea(attrs={'cols': 88, 'rows': 10, 'placeholder': 'Оставьте свой отзыв'})
        }
