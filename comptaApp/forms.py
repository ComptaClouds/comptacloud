from django import forms
from .models import User2
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CreationForm(forms.ModelForm):

    class Meta:
        model = User2
        fields = ('denomination', 'siege', 'objet', 'capital', 'duree',)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'secondname')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields