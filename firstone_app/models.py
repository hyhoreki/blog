from django.db import models

class Question(models.Model):
	qid=models.AutoField(primary_key=True)
	ask_user_id=models.IntegerField()
	question_title=models.CharField(max_length=120)
	question_describe=models.CharField(max_length=250)
	question_text=models.TextField()
	question_time=models.DateTimeField(auto_now=True)
	
	def  __str__(self):
		return self.question_title

class Attention_question(models.Model):
	aqid=models.AutoField(primary_key=True)
	question_id=models.IntegerField()
	attention_user_id=models.IntegerField()
	
class Answer(models.Model):
	aid=models.AutoField(primary_key=True)
	answer_user_id=models.IntegerField()
	answer_question_id=models.IntegerField()
	answer_text=models.TextField()
	answer_time=models.DateTimeField(auto_now=True)
	answer_agree=models.IntegerField(default=0)
	
	def __str__(self):
		return self.answer_text