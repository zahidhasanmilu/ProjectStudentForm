from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50, primary_key=True)
    dept=models.CharField(max_length=50, default="")
    sem=models.CharField(max_length=50, default="")
    email=models.CharField(max_length=50, default="")
    password=models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name