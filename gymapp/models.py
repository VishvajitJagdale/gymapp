from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    membership_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
