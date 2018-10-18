from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class BlogPost(models.Model):
    name = models.CharField(max_length=200, default='name')
    blogTitle = models.CharField(max_length=200)
    blogEntry = models.CharField(max_length=500)
    DateItWasCreated =models.DateTimeField(default=datetime.now)
    username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name