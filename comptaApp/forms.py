from django import forms

from .models import User2


class CreationForm(forms.ModelForm):

    class Meta:
        model = User2
        fields = ('denomination', 'siege', 'objet', 'capital', 'duree',)