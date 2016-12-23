from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
	lable="用户名",
	error_messages={'requirede':'请输入用户名'},
	widget=forms.TextInput(
	    attrs={
		'placeholder':"用户名",
	    }
	),
    )
    password = forms.CharField(
	required=True,
	lable="密码",
	error_messages={'required':'请输入密码'},
	widget=forms.TextInput(
	    attrs={
		'placeholder':"密码",
	    }
	),
    )
