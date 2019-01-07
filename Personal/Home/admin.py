from django.contrib import admin

from .models import Connector, PDF_Uploader

admin.site.register(Connector)
admin.site.register(PDF_Uploader)
