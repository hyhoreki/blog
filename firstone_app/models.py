from django.db import models

class Passage(models.Model):
	title = models.CharField(max_length=100)
	time = models.DateTimeField()
	content = models.CharField(max_length=10000)


