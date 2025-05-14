from django import forms
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class CommissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
