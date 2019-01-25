# System Imports
import json
import os
import sys
import re

# Add additional directories for imports
# Directories for PDF Parser application
current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_parser_directory = os.path.join(current_directory, 'PDF_Parser')
uploaded_files_directory = os.path.join(pdf_parser_directory, 'Uploaded_Files')
converted_files_directory = os.path.join(pdf_parser_directory, 'Converted_Files')

# Directories for Resume download
personal_directory = os.path.dirname(current_directory)
static_files_directory = os.path.join(personal_directory, 'static')
static_pdf_file_directory = os.path.join(static_files_directory, 'pdf')
resume_file_path = os.path.join(static_pdf_file_directory, 'Jarret_Laberdee_Resume.pdf')

# Directories for Employment Calculator
employment_calculator_dir = os.path.join(current_directory, 'Employment_Calculator')
employment_calculator_file = os.path.join(employment_calculator_dir, 'Employment_Calculator.py')


# Append them to the path so Django will recognize them
sys.path.append(pdf_parser_directory)
sys.path.append(uploaded_files_directory)
sys.path.append(converted_files_directory)
sys.path.append(static_files_directory)
sys.path.append(static_pdf_file_directory)
sys.path.append(employment_calculator_dir)

# Django Imports
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import smart_str
from django.core.mail import send_mail
from django.template import RequestContext
from django.template.loader import get_template, render_to_string

# Local Imports
from . forms import ConnectForm, PDF_Upload_Form
from . random_word_generator import generate_random_word, ajax_random_word
from . random_name_generator import Generator
from PDF_Parser import PDF_Handler, TextHandler
from Employment_Calculator import Employment_Calculator

def home(request):
    return render(request, 'home.html', {'navbar' : 'home'})

def about_me(request):

    calculator = Employment_Calculator()
    calculator.clear_logging_file()
    elapsed_time = calculator.calculate_elapsed_time()

    rendered_variables = {
        'navbar' : 'about_me',
        'elapsed_time' : elapsed_time,
    }

    return render(request, 'about_me.html', rendered_variables)

def download_resume(request):

    with open(resume_file_path, 'rb') as pdf:

        file = pdf.read()

        downloaded_file_name = 'Jarret-Laberdee-Resume.pdf'

        response = HttpResponse(content=file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}'.format(downloaded_file_name)

        pdf.close()

        return response

def connect(request):
    
    if request.method == 'POST':

        first_name = None
        last_name = None
        email = None
        body = None

        form = ConnectForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']

            form.save()

            form_variables = {
                'first_name' : first_name, 
                'last_name' : last_name, 
                'email' : email, 
                'body' : body,
                }

            # Email Preferences
            connect_response_email_to_submitter = render_to_string('email/connect_response.html', form_variables)

            personal_email = 'Jlamborghini22@gmail.com'

            # Send email to the submitter
            submitter_email_subject = '*Ding Ding*'
            submitter_text_argument = 'For some reason a text file was submitted. Uh oh.'

            send_mail(
                submitter_email_subject,
                submitter_text_argument,
                personal_email,
                [email],
                html_message=connect_response_email_to_submitter,
                fail_silently=False
            )


            return render(request, 'thank_you.html', {'form_variables' : form_variables, 'navbar' : 'connect'})
        
        else:
            form = ConnectForm()
            return render(request, 'connect.html', {'form' : form, 'navbar' : 'connect'})
    else: 
        form = ConnectForm()
        return render(request, 'connect.html', {'form' : form, 'navbar' : 'connect'})


    return render(request, 'connect.html', {'form':form, 'navbar' : 'connect'})

def projects(request):
    return render(request, 'project_home_page.html', {'navbar' : 'projects'})

def random_word_generator(request):
    context = {'random_word' : generate_random_word, 'navbar' : 'projects'}
    if request.method == 'GET':
        return render(request, 'random_word_generator.html', context)
    else:
        return render(request, 'random_word_generator.html', {'navbar' : 'projects'})

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

    pdf_handler = PDF_Handler()

    sanitize_filename_regex = r'[\\/:"*?<>|()]+'
    
    if request.method == 'POST':

        form = PDF_Upload_Form(request.POST, request.FILES)

        pdf_handler.write_logging_header()

        pdf_handler.check_and_create_folders()

        if form.is_valid():

            # Clear Converted Folder
            pdf_handler.clean_converted_folder()

            # Clear Uploaded Folder
            pdf_handler.clean_upload_folder()

            # Identify Uploaded File
            uploaded_file = request.FILES['file']
            uploaded_file_name = request.FILES['file'].name
            # uploaded_file_name = re.sub(sanitize_filename_regex, "", uploaded_file_name)

            # Dictate where file is to be uploaded
            fs = FileSystemStorage(
                location=uploaded_files_directory,
                base_url = '/media/'
                )
            
            # Provide Uploaded file a name
            fs.save(
                name=uploaded_file_name,
                content=uploaded_file
            )

            # Feed variaable into template engine
            context = {
                'file' : uploaded_file,
                'name' : uploaded_file.name
            }

            # Find Text Files
            # pdf_handler.find_txt_files()

            # Delete Text Files
            # pdf_handler.delete_unecessary_txt_files()

            # Find PDF Files
            pdf_handler.find_pdf_files()

            # Convert PDF Files into TXT
            pdf_handler.convert_pdf_to_txt()

            # Move Converted TXT File into Converted Folder
            pdf_handler.move_converted_files_into_converted_folder()

            pdf_handler.write_logging_footer()

            return redirect('display_content')
        else:
            form = PDF_Upload_Form()
            print('Form Invalid')
            return render(request, 'pdf_parser.html', {'form' : form, 'navbar' : 'projects'})

    else:
        form = PDF_Upload_Form()
        return render(request, 'pdf_parser.html', {'form' : form, 'navbar' : 'projects'})



    return render(request, 'pdf_parser.html', {})

def display_content(request):

    # Identify the file in the directory
    converted_directory_contents = os.listdir(converted_files_directory)
    converted_file = os.path.join(converted_files_directory, converted_directory_contents[0])
    converted_file_name = converted_directory_contents[0]

    f = open(converted_file, 'r')

    file_content = f.read()

    f.close()

    context = {'contents' : file_content, 'file_name' : converted_file_name, 'navbar' : 'projects'}

    return render(request, 'display_content.html', context)

# Create error views

def test_500(request):

    url_var = request.get_full_path()
    print(url_var)
    return render(request, 'error/500.html', {'url_var' : url_var})

# 404 - Page Not Found
def error_404(request):

    url_var = request.get_full_path()
    print(url_var)
    return render(request, 'error/404.html', {'url_var' : url_var})

# 500 - Internal Server Error
def error_500(request):
    url_var = request.get_full_path()
    print(url_var)
    return render(request, 'error/500.html', {'url_var' : url_var})


# 403 - Permission Denied

# 400 - Bad Request

    