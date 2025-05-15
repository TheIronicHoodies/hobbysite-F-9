from django.db import models
from django.urls import reverse
from user_management.models import Profile

cascade = models.CASCADE

STATUS_CHOICES_COMMISSION = {
    'OPEN': 'Open',
    'FULL': 'Full',
    'COMPLETED': 'Completed',
    'DISCONTINUED': 'Discontinued',
}

STATUS_CHOICES_JOB = {
    'OPEN': 'Open',
    'FULL': 'Full',
}

STATUS_CHOICES_JOBAPPLICATION = {
    'PENDING': 'Pending',
    'ACCEPTED': 'Accepted',
    'REJECTED': 'Rejected',
}

class Commission(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=cascade, null=True)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES_COMMISSION, default=list(STATUS_CHOICES_COMMISSION)[0])
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on',]
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.pk)])


class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=cascade)
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField(null=False)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES_JOB, default=list(STATUS_CHOICES_JOB)[0])

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

    def manpower_left(self):
        filled = JobApplication.objects.filter(job=self.id, status='ACCEPTED').count()
        return self.manpower_required - filled
    
    def get_absolute_url(self):
        return reverse('commissions:job', args=[str(self.pk)])


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=cascade, related_name='job_application')
    applicant = models.ForeignKey(Profile, on_delete=cascade)

    status = models.CharField(max_length=8, choices=STATUS_CHOICES_JOBAPPLICATION, default=list(STATUS_CHOICES_JOBAPPLICATION)[0])
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']

    def get_absolute_url(self):
        return reverse('commissions:job_application', args=[str(self.pk)])


class Comment(models.Model):
    commission = models.ForeignKey(Commission, null=False, on_delete=cascade, related_name='comments')
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on',]
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return str(self.entry)
    
    def get_absolute_url(self):
        return reverse('commissions:comment', args=[str(self.pk)])
