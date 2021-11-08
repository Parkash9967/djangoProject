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


class Scholarships(models.Model):
    scholarship_name = models.CharField(max_length=100, blank=True)
    scholarship_url = models.CharField(max_length=100, blank=True)
    scholarship_university = models.CharField(max_length=100, blank=True)
    scholarship_deadline = models.CharField(max_length=100, blank=True)
    scholarship_country = models.CharField(max_length=100, blank=True)
    scholarship_Start_date = models.CharField(max_length=100, blank=True)
    scholarship_program = models.CharField(max_length=100, blank=True)