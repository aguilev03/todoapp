from django import forms
from todoapp.models import Task, Notes
from django.contrib.auth.models import User


PRIORITY_CHOICE = [ tuple([x,x]) for x in range(1,6) ]
CATEGORY_CHOICE = [
    ('Facility','Facility'),
    ('IT','IT'),
    ('Kaizen','Kaizen'),
    ('Machine Down','Machine Down'),
    ('Machine Calibration','Machine Calibration'),
    ('Maintenance General','Maintenance General'),
    ('Maintenance Scheduled','Maintenance Scheduled'),
    ('Production','Production'),
    ('Programming PLC','Programming PLC'),
    ('Programming Python','Programming Python'),
    ('Programming VFE','Programming VFE'),
    ('Quality','Quality'),
    ('Technical Operations','Technical Operations'),
    ('Tooling Crimp','Tooling Crimp'),
    ('Tooling Seal','Tooling Seal'),
    ('Tooling VFE','Tooling VFE'),
    ('None', 'None')
]
USER_LIST =[
    ('evan','evan'),
    ('terell','terell'),
    ('tony','tony')
]

STATUS_LIST = [
    ('Not Started','Not Started'),
    ('In Progress','In Progress'),
    ('On Hold','On Hold'),
    ('Waiting','Waiting'),
    ('Complete','Complete')
]


class TaskForm(forms.ModelForm):
    



    class Meta:
        model = Task
        fields = ('author', 'subject', 'priority','text', 'due_date', 'assign', 'status', 'category', 'sub_category')
        

        widgets = {
            'subject': forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'priority' : forms.Select(choices=PRIORITY_CHOICE),
            'category' : forms.Select(choices=CATEGORY_CHOICE),
            'sub_category' : forms.Select(choices=CATEGORY_CHOICE),
            'assign' : forms.Select(choices=USER_LIST),
            'due_date' : forms.TextInput(attrs={'id':"datepicker"}),
            'status' : forms.Select(choices=STATUS_LIST)
            }

class NotesForm(forms.ModelForm):
    
    class Meta():
        model = Notes
        fields = ('author', 'text')
        widgets = {
            'author' : forms.Select(choices=USER_LIST),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }