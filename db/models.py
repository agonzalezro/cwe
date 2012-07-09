from django.db import models

from django_countries import CountryField


class Sector(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    url = models.URLField()
    sector = models.ForeignKey(Sector)
    employees = models.IntegerField()

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=128)
    activity = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=128)
    country = CountryField()
    profession = models.CharField(max_length=128)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class Politician(models.Model):
    name = models.CharField(max_length=128)
    country = CountryField()
    function = models.CharField(max_length=128)
    url = models.URLField()

    def __unicode__(self):
        return self.name
