from django import forms
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ["title", "author", "description", "status"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["role", "manpower_required", "status"]

class CommissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ["title", "author", "description", "status"]

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["role", "manpower_required", "status"]

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job',]