# System Imports
import os
import sys

# Django Imports
from django import forms


# local imports
from .models import Connector, PDF_Uploader

class ConnectForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", max_length=50)
    first_name.widget.attrs.update({'class': 'form-control', 'id' : 'connect_page_form_first_name'})

    last_name = forms.CharField(label="Last Name", max_length=50)
    last_name.widget.attrs.update({'class': 'form-control', 'id' : 'connect_page_form_last_name'})
    
    email = forms.EmailField(widget=forms.EmailInput, label="Email Address", max_length=100)
    email.widget.attrs.update({ 'class' : 'form-control', 'id' : 'connect_page_form_email'})
    
    body = forms.CharField(widget=forms.Textarea, label="Subject")
    body.widget.attrs.update({ 'class' : 'form-control', 'id' : 'connect_page_form_body', 'rows' : '5'})

    class Meta:
        model = Connector
        fields = ('first_name', 'last_name', 'email', 'body')

class PDF_Upload_Form(forms.Form):
    title = forms.CharField(max_length=50)
    title.widget.attrs.update({'class' : 'form-control', 'id' : 'pdf_parser_file_upload_form_title', 'placeholder' : 'Please Enter a Title to associate with this upload.'})

    file = forms.FileField()
    file.widget.attrs.update({'class' : 'form-control', 'id' : 'pdf_parser_file_upload_form_file_upload'})

    class Meta:
        model = PDF_Uploader
        fields = {'title', 'file'}

