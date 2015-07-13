from django.db import models

# Create your models here.


class Morir(models.Model):
    year = models.IntegerField(max_length=4, null=True)
    country = models.CharField(max_length=7, null=True)
    sex = models.CharField(max_length=8, null=True)
    cause_of_death = models.CharField(max_length=200, null=True)
    number_of_deaths = models.IntegerField(max_length=9, null=True)

    def __unicode__(self):
        return self.cause_of_death

    class Meta:
        verbose_name ='French death'
        verbose_name_plural = 'French deaths'