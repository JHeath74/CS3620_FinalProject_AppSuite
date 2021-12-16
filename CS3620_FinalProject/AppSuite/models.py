from django.db import models


# Create your models here.

class Hiking(models.Model):

    def __str__(self):
        return self.Hike_Name

    Hike_Name = models.CharField(max_length=200)
    Hike_Length = models.CharField(max_length=100)
    Hike_TrailType = models.CharField(max_length=100)
    Hike_TimeOfYear = models.CharField(max_length=200)
    Hike_Difficulty = models.CharField(max_length=200)
    Hike_TrailHead = models.CharField(max_length=500)
    Hike_Completed = models.CharField(max_length=25)
    Hike_Notes = models.TextField(max_length=5000)
    Hike_Images = models.ImageField(upload_to='images/')


class Journal(models.Model):

    def __str__(self):
        return self.Date_Time

    Date_Time = models.TextField(max_length=200)
    Journal_Entry = models.TextField(max_length=5000)


class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.CharField(max_length=1000)
    skills = models.CharField(max_length=200)


class Youtube(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    url = models.URLField(max_length=1000)
