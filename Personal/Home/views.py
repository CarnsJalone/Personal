# System Imports
import json

# Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize

# Local Imports
from . forms import ConnectForm
from . random_word_generator import generate_random_word, ajax_random_word
from . random_name_generator import Generator

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

    

