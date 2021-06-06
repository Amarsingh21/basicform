from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=100)
    Second_name = forms.CharField(max_length=100 )
    Mobile_No = forms.CharField(max_length = 13 )
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
