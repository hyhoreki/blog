from django.db import models

class Question(models.Model):
	qid=models.AutoField(primary_key=True)
	ask_user_id=models.IntegerField(null=True)
	question_title=models.CharField(max_length=120)
	question_describe=models.CharField(max_length=250)
	question_text=models.TextField()
	
	def  __str__(self):
		return self.question_title
		
class Answer(models.Model):
	aid=models.AutoField(primary_key=True)
	answer_user_id=models.IntegerField(null=True)
	answer_question_id=models.IntegerField()
	answer_text=models.TextField()
	answer_time=models.DateTimeField()
	
	def __str__(self):
		return self.answer_user_id