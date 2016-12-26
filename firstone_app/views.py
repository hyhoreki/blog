from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *

def index(request):
	return render(request, 'home.html')
def add(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))
def login(request):
	if request.method=='POST':
		username=request.POST.get('username', '')
		password=request.POST.get('password', '')
		user=auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect("/userpage/")
	return render(request, 'login.html')
def signup(request):
	if request.method=='POST':
		username=request.POST.get('username', '')
		password=request.POST.get('password', '')
		email=request.POST.get('email', '')
		if User.objects.filter(username=username):
			return render(request, 'signup.html', {'error': '1', 'error_message': '用户名已存在', 'username': username, 'password': password, 'email': email})
		elif User.objects.filter(email=email):
			return render(request, 'signup.html', {'error': '1', 'error_message': '该邮箱已被注册', 'username': username, 'password': password, 'email': email})
		else:
			user=User()
			user.username=username
			user.set_password(password)
			user.email=email
			user.first_name=username
			user.save()
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request, user)
				return HttpResponseRedirect("/userpage/")
	return render(request, 'signup.html')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/login/")
def userpage(request):
	if request.user is not None and request.user.is_active:
		if request.method=="POST":
			password_old=request.POST.get('password_old', '')
			password_new=request.POST.get('password_new1', '')
			nickname=request.POST.get('nickname', '')
			user=User.objects.get(username=request.user.username)
			if password_new == '' and password_old == password_new:
				user.first_name=nickname
				user.save()
				auth.login(request, user)
				return render(request, 'userpage.html', {'error': 0})
			if auth.authenticate(username=request.user.username, password=password_old):
				user.set_password(password_new)
				user.first_name=nickname
				user.save()
				auth.logout(request)
				return HttpResponseRedirect("/login/")
			else:
				return render(request, 'userpage.html', {'error': 1, 'error_message': '旧密码错误'})
		return render(request, 'userpage.html')
	else:
		return HttpResponseRedirect("/login/")

def blog_index(request):
	if request.user is not None and request.user.is_active:
		return render(request, 'blog_index.html')
	else:
		return HttpResponseRedirect("/login/")

def question_update(request):
	if request.user is not None and request.user.is_active:
		if request.method=="POST":
			user_id=request.user.id
			question_title=request.POST.get('question_title','')
			question_describe=request.POST.get('question_describe','')
			question_text=request.POST.get('question_text','')
			Questions.objects.create(ask_user=user_id, question_title=question_title, question_describe=question_describe, question_text=question_text)
		return render(request, 'question_update.html')
	else:
		return HttpResponseRedirect("/login/")