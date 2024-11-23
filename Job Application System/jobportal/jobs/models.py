from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posting_date = models.DateTimeField(default=datetime.now)
    screening_questions = models.TextField(blank=True, null=True)  # JSON-like string for questions

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    answers = models.TextField(blank=True, null=True)  # JSON-like string for answers
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"
