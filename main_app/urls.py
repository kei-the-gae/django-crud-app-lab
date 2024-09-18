from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('todos/', views.todo_index, name='todo_index'),
    path(
        'todos/add-todo/',
        views.add_todo,
        name='add_todo'
    ),
    path('todos/update/', views.update_todo, name='update_todo'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todo_delete'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='note_create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
]
