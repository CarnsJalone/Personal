# Generated by Django 2.1.3 on 2019-01-05 14:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF_Uploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/jarret/Documents/Python/Projects/Personal/Personal/Home/PDF_Parser/Uploaded_Files'), upload_to='')),
            ],
        ),
    ]
