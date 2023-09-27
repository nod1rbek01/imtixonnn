from django.db import models



class MyModel(models.Model):
    title = models.CharField(max_length=200)
    descriptoin = models.TextField()
    body = models.TextField()

    
