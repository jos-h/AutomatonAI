from django.db import models


def check_type():
    pass


class Tasks(models.Model):
    priority_choices = [
        ('Low', 'L'),
        ('Medium', 'M'),
        ('High', 'H'),
    ]
    user = models.CharField(max_length=255, default=True, null=True)
    goal = models.CharField(max_length=200)
    priority = models.CharField(choices=priority_choices, max_length=8)
    no_of_days = models.IntegerField()
