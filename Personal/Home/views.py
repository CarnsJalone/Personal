# System Imports
import json
import os
import sys

# Add additional directories for imports
current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_parser_directory = os.path.join(current_directory, 'PDF_Parser')
uploaded_files_directory = os.path.join(pdf_parser_directory, 'Uploaded_Files')
sys.path.append(pdf_parser_directory)
sys.path.append(uploaded_files_directory)

# Django Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.core.files.storage import FileSystemStorage

# Local Imports
from . forms import ConnectForm, PDF_Upload_Form
from . random_word_generator import generate_random_word, ajax_random_word
from . random_name_generator import Generator
from PDF_Parser import PDF_Handler

def home(request):
    return render(request, 'home.html', {})

def about_me(request):
    return render(request, 'about_me.html', {})

def connect(request):
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']

            form_variables = {
                'first_name' : first_name, 
                'last_name' : last_name, 
                'email' : email, 
                'body' : body
                }

            return render(request, 'thank_you.html', {'form_variables' : form_variables})
        
        else:
            form = ConnectForm()
            return render(request, 'connect.html', {'form' : form})
    else: 
        form = ConnectForm()
        return render(request, 'connect.html', {'form' : form})


    return render(request, 'connect.html', {'form':form})

def projects(request):
    return render(request, 'project_home_page.html', {})

def random_word_generator(request):
    context = {'random_word' : generate_random_word}
    if request.method == 'GET':
        return render(request, 'random_word_generator.html', context)
    else:
        return render(request, 'random_word_generator.html', {})

def random_word_generator_ajax(request):
    generate_random_word()
    random_word = generate_random_word()
    json_word = {'random_word' : random_word}
    return JsonResponse(json_word)

def random_name_generator(request):
    name_generator = Generator()
    randomly_generated_name = name_generator.generate_random_full_name()
    json_formatted_random_randomly_generated_name = {'randomly_generated_name' : randomly_generated_name}
    return JsonResponse(json_formatted_random_randomly_generated_name) 

def upload_pdf(request):

    upload_handler = PDF_Handler()
    
    if request.method == 'POST':
        form = PDF_Upload_Form(request.POST, request.FILES)

        if form.is_valid():

            uploaded_file = request.FILES['file']
            uploaded_file_name = request.FILES['file'].name

            context = {
                'file' : uploaded_file,
            }

            fs = FileSystemStorage()
            fs.save(uploaded_file_name, uploaded_file)

            return render(request, 'display_content.html', context)
        else:
            form = PDF_Upload_Form()
            print('Form Invalid')
            return render(request, 'pdf_parser.html', {'form' : form})

    else:
        form = PDF_Upload_Form()
        return render(request, 'pdf_parser.html', {'form' : form})



    return render(request, 'pdf_parser.html', {})

def display_content(request):
    # uploaded_file = request.FILES['file'].name
    # context = {'uploaded_file' : uploaded_file}
    return render(request, 'display_content.html')

    