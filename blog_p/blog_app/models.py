from django.db import models

class BlogPost(models.Model):
    username = models.CharField(max_length=200)
    blogTitle = models.CharField(max_length=200)
    blogEntry = models.CharField(max_length=500)
    DateItWasCreated =models.DateField()