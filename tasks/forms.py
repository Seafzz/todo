from django import forms
from .models import Task
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-success'))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        field = ['bio', 'location', 'birth_date']