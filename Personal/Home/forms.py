from django import forms

# local imports
from .models import Connector

class ConnectForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    first_name.widget.attrs.update({'class': 'form-control', 'id' : 'connect_page_form_first_name'})

    last_name = forms.CharField(label="Last Name", max_length=50)
    last_name.widget.attrs.update({'class': 'form-control', 'id' : 'connect_page_form_last_name'})
    
    email = forms.EmailField(widget=forms.EmailInput, label="Email Address", max_length=100)
    email.widget.attrs.update({ 'class' : 'form-control', 'id' : 'connect_page_form_email'})
    
    body = forms.CharField(widget=forms.Textarea, label="Subject")
    body.widget.attrs.update({ 'class' : 'form-control', 'id' : 'connect_page_form_body'})

    class Meta:
        model = Connector
        fields = ('first_name', 'last_name', 'email', 'body')