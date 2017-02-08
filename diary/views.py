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
			return render(request, 'diary_index.html')
		else:
			return render(request, 'diary_index.html', {'diary_create': '0'})
	else:
		return HttpResponseRedirect("/login/")