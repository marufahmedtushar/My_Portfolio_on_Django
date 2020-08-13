from django.db import models

# Create your models here.
class project(models.Model):
    project_id = models.AutoField
    project_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100,default="")
    project_title = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="img",default="")

    def __str__(self):
        return self.project_name


class skill(models.Model):
    skill_id = models.AutoField
    skill_name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="img",default="")

    def __str__(self):
        return self.skill_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    msg = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name