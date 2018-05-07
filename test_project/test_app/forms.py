from django import forms
from test_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic' )




#First form created using .Form
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
