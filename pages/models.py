from django.db import models

# Create your models here.

class Contact(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100, blank=True)
    Message = models.TextField(max_length=5000)

    def __str__(self):
        return self.Fullname