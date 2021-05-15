from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()


class AddForm(forms.Form):
    site = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
