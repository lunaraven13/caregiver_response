from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Situation(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Response(models.Model):
    response = models.ForeignKey(Situation)
    answer = models.CharField(max_length=128)
    # url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class webform(models.Model):
    webform = models.CharField(max_length=140)

    def __unicode__(self):
        return self.answer