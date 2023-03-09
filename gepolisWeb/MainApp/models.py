from django.db import models

class Projects(models.Model):
    name = models.TextField(max_length=100)
    desc = models.TextField(max_length=5000)
    image = models.TextField(max_length=100)
    use = models.TextField(max_length=1000)
    days = models.IntegerField(max_length=3)
    resault = models.TextField(max_length=100)

class Tages(models.Model):
    title = models.TextField(max_length=25)
    color = models.TextField(max_length=7)

class ProjectTages(models.Model):
    projectId = models.IntegerField(max_length=11)
    tageId = models.IntegerField(max_length=11)