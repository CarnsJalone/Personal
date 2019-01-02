from django.shortcuts import render
from django.http import HttpResponse

# Local Imports
from . forms import ConnectForm
from . random_word_generator import generate_random_word

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
        random_word = request.GET.get('random_word')
        return render(request, 'random_word_generator.html', context)
    else:
        return render(request, 'random_word_generator.html', {})
