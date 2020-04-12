from django.contrib.auth.views import LoginView
from django.contrib import admin
from datetime import datetime
from app import forms



admin.site.site_header ="iClassroom Admin Managemnt System"
admin.site.index_title = "Welcome To Admin Management"
admin.site.site_title = "Primary Control Hub"

admin.site.login =  LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         )
