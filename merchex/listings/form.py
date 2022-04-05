from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

    