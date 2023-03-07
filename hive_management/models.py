from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Hive(models.Model):
    name = models.CharField('Hive Name', max_length=255)
    location = models.CharField('Location', max_length=255)
    description = models.TextField('Description')
    supers = models.IntegerField('Supers')
    frames = models.IntegerField('Frames')
    color = models.CharField('Color', max_length=7, default='#00ff3f')
    purpose = models.CharField('Purpose', max_length=50, default='Honey')
    strength = models.IntegerField('Strength', default=90, validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_on = models.DateField('Date')

class Inspection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateField()
    queen = models.BooleanField()
    eggs = models.BooleanField()
    open_brood = models.BooleanField()
    sealed_brood = models.BooleanField()
    honey = models.CharField(max_length=255)
    varroa = models.CharField(max_length=255)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateField()
    med_name = models.CharField(max_length=50)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)

class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    hive = models.ForeignKey('Hive', on_delete=models.CASCADE)
