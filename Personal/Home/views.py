from django.shortcuts import render
from django.http import HttpResponse

# Local Imports
from . forms import ConnectForm

def home(request):
    return render(request, 'home.html', {})

def resume(request):
    return render(request, 'resume.html', {})

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

            return HttpResponse('Yo')

        else:
            form = ConnectForm()
    else: 
        form = ConnectForm()


    return render(request, 'connect.html', {'form':form})
