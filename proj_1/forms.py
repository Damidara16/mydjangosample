from django import forms

class contactForm(forms.Form):
    email = forms.EmailField(required=True)
    fName = forms.CharField(required=True)
    lName = forms.CharField(required=True)
