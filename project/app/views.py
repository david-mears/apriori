from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from flatpickr import DatePickerInput
from flatpickr.utils import GenericViewWidgetMixin

from .models import Task
from .forms import TaskForm

class TaskList(ListView): 
    login_required = True
    model = Task
    fields = '__all__'

class TaskDetail(DetailView):
    login_required = True
    model = Task
    fields = '__all__'

class TaskCreate(CreateView): 
    login_required = True
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdate(UpdateView): 
    login_required = True
    model = Task
    form_class = TaskForm

class TaskDelete(DeleteView):
    login_required = True
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('home')
