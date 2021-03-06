from django.db import models

class Question(models.Model):
	qid=models.AutoField(primary_key=True)
	ask_user_id=models.IntegerField()
	question_title=models.CharField(max_length=30)
	question_describe=models.CharField(max_length=100)
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

class Agree_answer(models.Model):
	agid=models.AutoField(primary_key=True)
	answer_id=models.IntegerField(default=0)
	agree_user_id=models.IntegerField(default=0)

class Friend(models.Model):
	fid=models.AutoField(primary_key=True)
	friend_one=models.IntegerField(default=0)
	friend_two=models.IntegerField(default=0)
	friendship_status=models.IntegerField(default=0)