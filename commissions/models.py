from django.db import models

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    people_reqd = models.IntegerField(null=False)
    created_on = models.DateTimeField() # incomplete
    last_updated = models.DateTimeField() # incomplete

class Comment(models.Model):
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE)
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField() # incomplete
    last_updated = models.DateTimeField() # incomplete