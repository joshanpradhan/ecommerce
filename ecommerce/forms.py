from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=20, widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    last_name = forms.CharField(label='Last Name', max_length=20, widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            "class": "form-control"
        }))
    subject = forms.CharField(label='Subject', max_length=50, widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    message = forms.CharField(label='Message', max_length=500, widget=forms.Textarea(
        attrs={
            "class": "form-control"
        }))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter Password"}))


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username')
    new_password = forms.CharField(
        label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError("Passwords must match")
        return data
