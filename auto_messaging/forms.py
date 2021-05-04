from django import forms

CHOICES = [
    ('file','file'),
    ('input','input')
]
class Choice(forms.Form):
    input=forms.CharField(label='input', widget=forms.RadioSelect(choices=CHOICES))
