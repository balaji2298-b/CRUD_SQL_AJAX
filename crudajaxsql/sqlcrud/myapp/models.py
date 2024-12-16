from django.db import models


class Batmen(models.Model):
	name = models.CharField(max_length=20, null=True, blank=True)
	mobilenumber = models.CharField(max_length=10, null=True, blank=True)
	age = models.CharField(max_length=5, null=True, blank=True)
	city = models.CharField(max_length=20, null=True, blank=True)

