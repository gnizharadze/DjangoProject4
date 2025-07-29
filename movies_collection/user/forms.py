from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

class UsernameLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget= forms .TextInput(attrs={'placeholder':'Enter Username','class':'form-control'})
    )

    def __init__(self, request=None, *args, **kwargs): # Accept request argument
        super().__init__(request=request, *args, **kwargs)

        if 'password' in self.fields:    #passwordebis washla fields da base_fieldsidan
            del self.fields['password']

        if 'password' in self.base_fields:
            del self.base_fields['password']

    def clean(self):

        username = self.cleaned_data.get('username')

        if not username:
            raise forms.ValidationError("Please enter a username.")


        return self.cleaned_data