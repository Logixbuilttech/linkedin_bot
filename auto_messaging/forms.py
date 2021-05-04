from django import forms


class Choice(forms.Form):
    csv_upload = forms.BooleanField(required=False)

class FileUpload(forms.Form):
    csv_file = forms.FileField(required=False)

class Text_input(forms.Form):
    uname = forms.FileField(required=False)