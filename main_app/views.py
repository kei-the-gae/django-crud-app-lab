from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo, Note

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
            # return redirect('todo-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(req, 'signup.html', context)

def todo_index(req):
    todos = Todo.objects.all()
    notes = Note.objects.all()
    return render(req, 'todos/index.html', {'todos': todos, 'notes': notes})

def note_detail(req, note_id):
    note = Note.objects.get(id=note_id)
    return render(req, 'todos/notes/detail.html', {'note': note})
