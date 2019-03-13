from django.forms import ModelForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import Specialist,Recording





class SpecialistAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Specialist._meta.fields]



    class Meta:
        model = Specialist

admin.site.register(Specialist, SpecialistAdmin)

class RecordingAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Recording._meta.fields]



    class Meta:
        model = Recording

admin.site.register(Recording, RecordingAdmin)






