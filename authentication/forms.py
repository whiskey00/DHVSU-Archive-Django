from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': (""),
        'password_too_short': (""),
        'password_common': (""),
        'username': {
            'required': (""),
            'unique': (""),
            'invalid': (""),
        },
        'email': {
            'required': (""),
            'unique': (""),
            'invalid': (""),
        },
    }

    username = forms.CharField(label="", error_messages=error_messages, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(label="", error_messages=error_messages, required=True, widget=forms.EmailInput(attrs={"placeholder": "myemail@dhvsu.edu.ph"}))
    password1 = forms.CharField(label="", error_messages=error_messages, widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(label="", error_messages=error_messages, widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")

        # if not "dhvsu.edu.ph" in email:
        #     raise forms.ValidationError("Must be a DHVSU account!")
        
        return email
