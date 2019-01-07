# System Imports
import os
import sys

# Django Imports
from django.db import models
from django.core.files.storage import FileSystemStorage

# Add additional directories for imports
current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_parser_directory = os.path.join(current_directory, 'PDF_Parser')
uploaded_files_directory = os.path.join(pdf_parser_directory, 'Uploaded_Files')
sys.path.append(uploaded_files_directory)

# Storage Location for Uploaded Files
fs = FileSystemStorage(location=uploaded_files_directory)

class Connector(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} at {} sent you: \n {}'.format(self.first_name, self.last_name, self.email, self.body)

class PDF_Uploader(models.Model):

    title = models.CharField(max_length=50)
    file = models.FileField(default="")

    def __str__(self):
        return '{}'.format(self.title)


