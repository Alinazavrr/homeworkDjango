from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.utils import timezone
# Create your views here.
from .forms import TaskForm
from .models import Task

class TaskList(ListView):
    """
    Give list of tasks
    """

    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    """
    Give one task detail
    """

    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datetime = self.get_object().deadline
        context['overdue'] = True if timezone.now() < datetime else False
        return context


class TaskCreate(CreateView):
    """
    Create task model view
    """
    model = Task
    form_class = TaskForm
    template_name = 'toDoList/form.html'
    success_url = '/task/{id}'

class TaskUpdate(UpdateView):
    """
    Update task model View
    """
    model = Task
    template_name = 'toDoList/form.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        form = self.get_form_class()(instance=task)
        context['form'] = form
        return context

class TaskDelete(DeleteView):
    """
    Delete task view
    """
    model = Task
    template_name = 'toDolist/form.html'
    success_url = reverse_lazy('task_list')