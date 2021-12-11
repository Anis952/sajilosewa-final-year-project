from django import forms
from django.contrib.auth.models import User

# from core.models import Customer, Job

class BasicUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name')