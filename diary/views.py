from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
import json

def home(request):
	if request.user is not None and request.user.is_active:
		if Diary.objects.filter(diary_user_id=request.user.id):
			diary_info=Diary_Index_Info.objects.get(diary_user_id=request.user.id)
			return render(request, 'diary_index.html', {'diary_create': '1', 'title': diary_info.diary_title, 'bg_color': diary_info.diary_background_color, 'font_color': diary_info.diary_font_color, 'music': diary_info.diary_music})
		else:
			return render(request, 'diary_index.html', {'diary_create': '0'})
	else:
		return HttpResponseRedirect("/login/")

def create_diary(request, title, bg_color, font_color, music):
	Diary.objects.create(diary_user_id=request.user.id)
	diary=Diary.objects.get(diary_user_id=request.user.id)
	if Diary_Index_Info.objects.create(diary_id=diary.diary_id, diary_user_id=diary.diary_user_id, diary_title=title, diary_background_color='#'+bg_color, diary_font_color='#'+font_color, diary_music=music):
		create_status_dict={'status': '1'}
	else:
		create_status_dict={'status': '0'}
	create_status_dict_json=json.dumps(create_status_dict)
	return HttpResponse(create_status_dict_json, content_type='application/json')

def diary_title_set(request, new_title):
	diary=Diary_Index_Info.objects.get(diary_user_id=request.user.id)
	diary.diary_title=new_title
	diary.save()
	title_set={'error': '0'}
	title_set_json=json.dumps(title_set)
	return HttpResponse(title_set_json, content_type='application/json')
