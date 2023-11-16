from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    """
    Role in the logic of the quality system, in which editors,
    reviewers and submitters have different views
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    """
    In academics are different levels of seniority, like junior researcher,
    senior researcher, prof and so on
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roles = models.ManyToManyField(Role)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Notification(models.Model):
    message = models.CharField(max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField()
    seen = models.BooleanField()

