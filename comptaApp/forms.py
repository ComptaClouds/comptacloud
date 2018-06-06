from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User,Group





class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class CreationForm(forms.ModelForm):

    class Meta:
        model = User2
        fields = ('denomination', 'siege', 'objet', 'capital', 'duree',)


class fournisseurs(forms.ModelForm):

    class Meta:
        model = operationcompta
        fields = ('libelle',)


class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    image = forms.FileField(help_text="Upload image: ", required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'image', 'email','group', )

class DocumentForm(forms.ModelForm):
    entreprise = forms.ModelChoiceField(queryset=CustomUser.objects.filter(groups=1),
                                                required=True)

    class Meta:
        model = Document
        fields = ('description', 'document', 'entreprise',)

class autorisation(forms.ModelForm):
    utilise = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.filter(autorise=0),
                                   widget=forms.CheckboxSelectMultiple )

    class Meta:
        model = CustomUser
        fields = ('utilise',)


class CustomUserChangeForm(UserChangeForm):
   # image = forms.FileField(help_text="Upload image: ", required=False)
    #group = forms.ModelChoiceField(queryset=Group.objects.all(),
     #                             required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)


class continuerenregistrement(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


