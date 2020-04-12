from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'chat/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
