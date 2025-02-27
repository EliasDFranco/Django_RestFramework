from django.db import models

class Project(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField(max_length=200)
    technology = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add= True)
