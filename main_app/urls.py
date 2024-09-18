from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('todos/', views.todo_index, name='todo_index'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/create/', views.NoteCreate.as_view(), name='note_create'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
]
