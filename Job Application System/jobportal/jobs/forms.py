from django import forms
from .models import Application, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'screening_questions']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume', 'answers']
        widgets = {
            'answers': forms.Textarea(attrs={'placeholder': 'Answer screening questions here...'}),
        }
