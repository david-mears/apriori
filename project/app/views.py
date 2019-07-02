from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
from django.db.models import FloatField
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('density') == '1':
            context['algorithm'] = 'density'
            optimal_tasks = (
                Task.objects
                .annotate(density=(
                    Cast('importance', FloatField())/Cast('estimated_duration', FloatField())
                ))
                .order_by('done', '-density')
            )
            if len(optimal_tasks) != 0:
                context['first_task_benchmark'] = optimal_tasks[0].density
            context['optimal_tasks'] = optimal_tasks
        else:
            context['algorithm'] = 'shortest_processing_time'
            optimal_tasks = (
                Task.objects
                .order_by('done', 'estimated_duration')
            )
            if len(optimal_tasks) != 0:
                context['first_task_benchmark'] = optimal_tasks[0].estimated_duration
            context['optimal_tasks'] = optimal_tasks
        return context

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
