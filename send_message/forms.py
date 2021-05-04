from django import forms

class NameForm(forms.Form):
    profile_user_id = forms.CharField(label='profile_user_id')
    message_body = forms.CharField(label='message_body')

class CredsForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')
