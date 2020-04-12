"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=255, null=False, blank=False)
    description=models.TextField(blank=True,null=True)
    duration=models.DurationField(null=False)


# Create your models here.
class Attendence(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    attended=models.BooleanField()
    date=models.DateTimeField(auto_now_add=True)