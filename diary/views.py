from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
import json

def home(request):
	return render(request, 'diary_index.html')