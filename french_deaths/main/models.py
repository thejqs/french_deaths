from django.db import models

# Create your models here.


class Morir(models.Model):
    SEX_CHOICES = [
        ('Males', 'Males'),
        ('Females', 'Females')
    ]
    number_of_deaths = models.IntegerField(max_length=15, null=True)
    year = models.IntegerField(max_length=4, null=True)
    sex = models.CharField(max_length=8, choices=SEX_CHOICES, null=True)
    cause = models.ForeignKey('main.MorirCause', null=True)

    def __unicode__(self):
        return self.sex

    class Meta:
        verbose_name = 'French death'
        verbose_name_plural = 'French deaths'


class MorirCause(models.Model):
    cause = models.CharField(max_length=200, unique=True, null=True)

    def __unicode__(self):
        return self.cause

    class Meta:
        verbose_name = 'Causes of French death'
        verbose_name_plural = 'Causes of French deaths'


# class MorirSex(models.Model):
#     sex = models.CharField(max_length=8, null=True)

#     def __unicode__(self):
#         return self.sex

#     class Meta:
#         verbose_name = 'Sex of French death'
#         verbose_name_plural = 'Sex of French deaths'
