from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={"placeholder": "myemail@dhvsu.edu.ph"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

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

        if not "dhvsu.edu.ph" in email:
            raise forms.ValidationError("Must be a DHVSU account!")
        
        return email
