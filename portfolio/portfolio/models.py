from django.db import models

class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    dob = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=500,db_column='description')
    image = models.ImageField(null=True, blank=True, upload_to ="images/")


class Educations(models.Model):
    id = models.AutoField(primary_key=True)
    dept = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    result = models.CharField(max_length=20)
    institute = models.CharField(max_length=500)
    status = models.CharField(max_length=500)