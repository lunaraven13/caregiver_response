from django.db import models

# Create your models here.

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
        return self.answer