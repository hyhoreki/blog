from django.db import models

class Passage(models.Model):
	title = models.CharField(max_length=100)
	time = models.DateTimeField()
	content = models.CharField(max_length=10000)
	
	def __str__(self):
		return self.title
	
class Questions(models.Model):
	ask_user=models.IntegerField()
	answer_user=models.IntegerField()
	question_title=models.CharField(max_length=500)
	question_describe=models.CharField(max_length=500)
	question_text=models.CharField(max_length=3000)
	question_answer_text=models.CharField(max_length=3000)
	
	def  __str__(self):
		return self.question_title
