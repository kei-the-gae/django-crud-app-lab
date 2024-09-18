from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo, Note
from .forms import TodoForm

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def signup(req):
    error_message = ''
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('todo_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(req, 'signup.html', context)

@login_required
def todo_index(req):
    todo_form = TodoForm()
    todos = Todo.objects.filter(user=req.user)
    notes = Note.objects.filter(user=req.user)
    return render(req, 'todos/index.html', {'todo_form': todo_form, 'todos': todos, 'notes': notes})

@login_required
def add_todo(req):
    form = TodoForm(req.POST)
    if form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.user_id = req.user.id
        new_todo.save()
    return redirect('todo_index')

@login_required
def update_todo(req):
    form = req.body
    if form.is_valid():
        updated_todo = form
        updated_todo.user_id = req.user.id
        updated_todo.save()
    return redirect('todo_index')

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todos/'

@login_required
def note_detail(req, note_id):
    note = Note.objects.get(id=note_id)
    return render(req, 'todos/notes/detail.html', {'note': note})

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']
    success_url = '/todos/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'body']

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/todos/'
