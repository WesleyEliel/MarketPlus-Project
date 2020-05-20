from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.admin.widgets import AdminDateWidget
from .models import *
from django.contrib.auth.models import User

user = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'autocomplete':'new-password'}))


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'RePassword'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    """def save(self, commit=True):
        new_user = super(UserCreationForm, self).save(commit=False)
        new_user.set_password(self.cleaned_data["password1"])
        if commit:
            new_user.save()
        return new_user"""




"""
date_of_birth = forms.DateField(
        label = 'Date of Birth' ,
        help_text='Enter your Birthday following this format YYYY/MM/DD',
        widget=forms.SelectDateWidget(),
    )
        
    profession = forms.CharField(
        label = 'Profession',
        max_length=100,
        help_text="Help us to provide you analytics Articles",
    )

    postal_code = forms.CharField(
        label = 'Postal Code',
        max_length=40,
    )
    phone = forms.CharField(
        label = 'Phone',
        max_length=25,
    )
    country = forms.CharField(
        label = 'Country' ,
        max_length=20,
    )
    city_town = forms.CharField(
        label = 'City/Town' ,
        max_length=30,
    )

"""