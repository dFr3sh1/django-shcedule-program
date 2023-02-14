from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields =('username', 'email', 'first_name', 'last_name', 'role')


class LoginForm(forms.Form):
    """
    Form class with one parameter from forms.

    Args:
        forms (_Form_): take two arguments to access user to the site
    """
    username = forms.CharField(max_length=70, label="Nom d'utilisateur")
    password = forms.CharField(max_length=8, widget=forms.PasswordInput, label='Mot de passe')
