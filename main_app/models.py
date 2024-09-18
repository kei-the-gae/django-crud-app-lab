from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField('', default=False)
    text = models.CharField('', max_length=100)
    def __str__(self):
        return f'{self.text}, is complete: {self.checked}'
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField('')
    def __str__(self):
        return f'{self.title}: {self.body}'
    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"note_id": self.id})
