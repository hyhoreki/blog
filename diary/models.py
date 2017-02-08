from django.db import models

class Diary(models.Model):
	diary_id=models.AutoField(primary_key=True)
	diary_user_id=models.IntegerField(default=0)

class Diary_Index_Info(models.Model):
	diary_index_info_id=models.AutoField(primary_key=True)
	diary_id=models.IntegerField(default=0)
	diary_user_id=models.IntegerField(default=0)
	diary_title=models.CharField(max_length=12)
	diary_backgroud_mode=models.IntegerField(default=0)
	diary_background_color=models.CharField(max_length=10)
	diary_background_img=models.TextField()
	diary_music=models.TextField()