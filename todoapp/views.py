from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from todoapp.models import Task, Notes
from todoapp.forms import TaskForm, NotesForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

all_list = Task
user_list = Task
active_list = Task
# Create your views here.
def task_list_system(request):
    return render(request, 'todoapp/task_list.html',{}) 

class TaskListView(ListView):
    model = all_list

    def get_unfiltered_queryset(self):
        return Task.objects.all()

class TaskDetailView(DetailView):
    model = Task

class CreateTaskView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'todoapp/task_detail.html'
    form_class = TaskForm
    model = Task

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'todoapp/task_detail.html'
    form_class = TaskForm
    model = Task

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

class TaskActiveListView(LoginRequiredMixin, ListView):
    model = active_list

    def get_queryset(self):
        return Task.objects.exclude(status="Complete").order_by('-due_date')

class TaskUserListView(LoginRequiredMixin, ListView):
    model = user_list

    def get_queryset(self):
        return Task.objects.exclude(status="Complete").filter(assign=self.request.user).order_by('-due_date')



#########################################
#########################################

@login_required
def add_note_to_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.task = task
            note.save()
            return redirect('task_detail',pk=task.pk)
    else:
        form = NotesForm()

    return render(request,'todoapp/note_form.html',{'form':form})

@login_required
def note_remove(request,pk):
    note = get_object_or_404(Notes, pk=pk)
    task_pk = note.task.pk
    note.delete()
    return redirect('task_detail', pk=task_pk)