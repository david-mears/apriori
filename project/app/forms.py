from .models import Task
from django import forms
from flatpickr import DatePickerInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': DatePickerInput(),
        }