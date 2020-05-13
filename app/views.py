"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from app.forms import SignUpForm

@login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def signup(request):
    print("Signup Page")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})
    

@login_required
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'iClassroom',
            'year':datetime.now().year,
        }
    )

def maintainance_404(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/404.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

