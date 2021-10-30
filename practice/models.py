from django.db import models

# Create your models here.
from django.db import models


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=100, blank=True)
    firstname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        print('save() is called.')
        super(Students, self).save(*args, **kwargs)
