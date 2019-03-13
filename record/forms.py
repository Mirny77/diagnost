from django import forms
from .models import Specialist,Recording
from django.contrib.admin import widgets


class RecordingForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ('date','time','name','brand')

