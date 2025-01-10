from django import forms
from .models import Task


class TaskCreateinForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_task',]
        labels = {'name_task':'nova tarefa'}
    
        widgets = {
            'name_task' : forms.TextInput(attrs={'class':'form-control',
            'style': 'width: 300px;',
            }),
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_task',]
        labels = {'name_task':'atualizar tarefa'}
    
        widgets = {
            'name_task' : forms.TextInput(attrs={'class':'form-control',
            'style': 'width: 300px;',
            }),
        }
