from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from admin_exam.models import UserInfo
import re


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text",
            'name': "username"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input100",
            'type': "password",
            'name': "pass"
        }))

    def clean(self):
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'])
        if not user:
            raise forms.ValidationError(
                "Tên tài khoản hoặc mật khẩu không chính xác !!!")


class RegisterForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text",
            'name': "username"
        }))
    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "email",
            'name': "email"
        }))
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text"
        }))
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input100",
            'type': "password"
        }))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input100",
            'type': "password"
        }))
    birth_day = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text",
            'readonly': "readonly",
            'data-toggle': "datepicker"
        }))
    phone_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text"
        }))
    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "input100",
            'type': "text"
        }))

    def clean_confirm_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']

            if password == confirm_password and password:
                return confirm_password

            if len(password) < 6 and len(password) >= 30:
                raise forms.ValidationError("Mật khẩu từ 6 đến 30 ký tự")

        raise forms.ValidationError("Xác nhận mật khẩu không chính xác !!!")

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\W+$', username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt !!!")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại !!!")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
        )
