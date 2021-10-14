from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length = 100, label = 'Name')
    email = forms.EmailField(required = False, label = 'e-mail address')
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)