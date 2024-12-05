from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']