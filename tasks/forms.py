from django import forms
from .models import Task


class TaskCreateinForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_task']
    
        widgets = {
            'name_tasks' : forms.TextInput(attrs={'class':'form-control'}),
        }
