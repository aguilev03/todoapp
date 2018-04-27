from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Task(models.Model):
    author = models.ForeignKey('auth.User')
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True)
    assign = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='Not Started')
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, default='5')
    def set_due(self):
        self.due_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.subject

class Notes(models.Model):
    task = models.ForeignKey('todoapp.Task',related_name='notes')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_note = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('task_list')

    def __str__(self):
        return self.text

