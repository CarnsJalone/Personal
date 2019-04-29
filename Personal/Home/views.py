# System Imports
import json
import os
import sys
import re
import logging

# Add additional directories for imports
current_directory = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(current_directory)

# Directories for Mail application
child_personal_directory = os.path.join(BASE_DIR, "Personal")
# settings_file_path = os.path.join(child_personal_directory, "settings.py")

# Directories for PDF Parser application
pdf_parser_directory = os.path.join(current_directory, 'PDF_Parser')
uploaded_files_directory = os.path.join(pdf_parser_directory, 'Uploaded_Files')
converted_files_directory = os.path.join(pdf_parser_directory, 'Converted_Files')

# Directories for Resume download
personal_directory = os.path.dirname(current_directory)
VISITOR_LOGS_DIRECTORY = os.path.join(current_directory, 'visitorLogs')
static_files_directory = os.path.join(personal_directory, 'static')
static_pdf_file_directory = os.path.join(static_files_directory, 'pdf')
resume_file_path = os.path.join(static_pdf_file_directory, 'Jarret_Laberdee_Resume.pdf')
logger = os.path.join(static_files_directory, 'txt/logger.txt')
JSON_DIR = os.path.join(static_files_directory, 'json')
MP4_DIR = os.path.join(static_files_directory, "mp4")

# Directories for Employment Calculator
employment_calculator_dir = os.path.join(current_directory, 'Employment_Calculator')
employment_calculator_file = os.path.join(employment_calculator_dir, 'Employment_Calculator.py')

# If I were more thoughtful, I wouldn't hardcode this, but meh, yolo swag
GCPAPIKEY = "AIzaSyASSZA3KJq9J3hWHJzvV7YWsm6g1VVXa94"

# Append them to the path so Django will recognize them
sys.path.append(VISITOR_LOGS_DIRECTORY)
sys.path.append(child_personal_directory)
sys.path.append(pdf_parser_directory)
sys.path.append(uploaded_files_directory)
sys.path.append(converted_files_directory)
sys.path.append(static_files_directory)
sys.path.append(static_pdf_file_directory)
sys.path.append(employment_calculator_dir)
sys.path.append(JSON_DIR)
sys.path.append(MP4_DIR)

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
from Personal import settings
from visitorLogUpdater import updateAccessLogs
from visitorLogExtractor import returnVisitorDataFromDatabase

# logging.basicConfig(filename=logger, level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename=logger, format='%(asctime)s\n %(levelname)s %(message)s',datefmt='%H:%M:%S') 

def home(request):

    rendered_variables = {
        'navbar' : 'home',
    }

    return render(request, 'home.html', rendered_variables)

def about_me(request):

    calculator = Employment_Calculator()
    calculator.write_logging_header()
    elapsed_time = calculator.calculate_elapsed_time()
    calculator.write_logging_footer()

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

    path_to_json_file = os.path.join(JSON_DIR, 'input_error.json')

    with open(path_to_json_file) as json_data:
        input_error_json = json.loads(json_data.read())
    
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

                personal_email = settings.EMAIL_HOST_USER

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


                return render(request, 'thank_you.html', {'form_variables' : form_variables, 'navbar' : 'connect', 'input_error_json' : input_error_json})
            
            else:
                form = ConnectForm()
                return render(request, 'connect.html', {'form' : form, 'navbar' : 'connect', 'input_error_json' : input_error_json})
        else: 
            form = ConnectForm()
            return render(request, 'connect.html', {'form' : form, 'navbar' : 'connect', 'input_error_json' : input_error_json})


        return render(request, 'connect.html', {'form':form, 'navbar' : 'connect', 'input_error_json' : input_error_json})

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

    f = open(converted_file, 'r', encoding='utf-8')

    file_content = f.read()

    f.close()

    rendered_variables = {
        'contents' : file_content, 
        'file_name' : converted_file_name,
        'navbar' : 'projects'
        }

    return render(request, 'display_content.html', rendered_variables)

def reaction_time_test(request):

    path_to_json_file = os.path.join(JSON_DIR, 'reaction_time_percentile.json')

    with open(path_to_json_file) as json_data:
        reaction_time_json = json.loads(json_data.read())

        rendered_variables = {
            'reaction_times' : reaction_time_json, 
            'navbar' : 'projects'
        }

        return render(request, 'reaction_time_test.html', rendered_variables)

def linkedin_bot(request):

    rendered_variables = {
        'navbar' : 'projects'
    }

    return render(request, 'linkedin_bot.html', rendered_variables)

def access_log_visualizer(request):

    visitorData = returnVisitorDataFromDatabase()
    visitorData = json.dumps(visitorData)

    rendered_variables = {
        'navbar' : 'projects', 
        'maps_api_key' : GCPAPIKEY, 
        'visitorData' : visitorData
    }

    return render(request, 'access_log_visualizer.html', rendered_variables)

def update_access_logs(request):

    if not request.user.is_authenticated:
        return redirect('/admin')

    return render(request, 'admin_templates/update_access_logs.html', {})

def update_access_logs_triggered(request):

    if request.method == "GET":
        stackTrace = updateAccessLogs()

        json_update_message = {
        'status' : 'Updating...',
        'stackTrace' : stackTrace
    }

        return JsonResponse(json_update_message)

# Create error views

def test_500(request):

    url_var = request.get_full_path()
    print(url_var)
    return render(request, 'error/500.html', {'url_var' : url_var})

# 404 - Page Not Found
def error_404(request):

    url_var = request.get_full_path()

    rendered_variables = {
        'url_var' : url_var,
        'me_living_life' : False
    }
    
    return render(request, 'error/404.html', rendered_variables)

# 500 - Internal Server Error
def error_500(request):

    url_var = request.get_full_path()

    rendered_variables = {
        'url_var' : url_var,
        'me_living_life' : False
    }

    return render(request, 'error/500.html', rendered_variables)


# 403 - Permission Denied

# 400 - Bad Request

    