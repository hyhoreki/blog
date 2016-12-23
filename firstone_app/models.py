from django.db import models

class Passage(models.Model):
	title = models.CharField(max_length=100)
	time = models.DateTimeField()
	content = models.CharField(max_length=10000)
	
class Questions(models.Model):
	ask_user=models.IntergerField()
	answer_user=models.IntergerField()
	question_title=models.CharField(max_length=500)
	question_text=models.CharField(max_length=3000)
	question_answer_text=models.CharField(max_length=3000)


