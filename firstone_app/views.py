from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
import json

def index(request):
	return render(request, 'home.html')
	
def login(request):
	if request.method=='POST':
		username=request.POST.get('username', '')
		password=request.POST.get('password', '')
		user=auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect("/userpage/")
		else:
			return render(request, 'login.html', {'error': '1', 'error_message': '用户名密码错误'})
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

def blog_index(request, select_id):
	if request.user is not None and request.user.is_active:
		questions=Question.objects.all().order_by('?')[:5]
		return render(request, 'blog_index.html', {'questions':questions, 'select_id':select_id})
	else:
		return HttpResponseRedirect("/login/")

def question_update(request):
	if request.user is not None and request.user.is_active:
		if request.method=="POST":
			user_id=request.user.id
			question_title=request.POST.get('question_title', '')
			question_describe=request.POST.get('question_describe', '')
			question_text=request.POST.get('question_text', '')
			Question.objects.create(ask_user_id=user_id, question_title=question_title, question_describe=question_describe, question_text=question_text)
			question=Question.objects.get(question_title=question_title, question_describe=question_describe, question_text=question_text)
			return HttpResponseRedirect('/question/' + str(question.qid) + '/')
		else:
			return render(request, 'question_update.html')
	else:
		return HttpResponseRedirect("/login/")
		
def question_show(request, qid):
	if request.user is not None and request.user.is_active:
		question=Question.objects.get(qid=qid)
		ask_user=User.objects.get(id=question.ask_user_id)
		if Attention_question.objects.filter(question_id=qid, attention_user_id=request.user.id):
			attention_status = 1
		else:
			attention_status = 0
		if request.method=="POST":
			answer_user_id=request.user.id
			answer_text=request.POST.get('answer_text', '')
			Answer.objects.create(answer_user_id=answer_user_id, answer_question_id=qid, answer_text=answer_text)
			return HttpResponseRedirect(request.path)
		if Answer.objects.filter(answer_question_id=qid):
			answer=Answer.objects.filter(answer_question_id=qid).order_by('?')[0]
			answer_user=User.objects.get(id=answer.answer_user_id)
			return render(request, 'question_show.html', {'qid':qid, 'question_title':question.question_title, 'question_text':question.question_text, 'ask_user_nickname':ask_user.first_name, 'ask_user_id':answer.answer_user_id, 'answer_text':answer.answer_text, 'answer_time':answer.answer_time, 'answer_user_nickname':answer_user.first_name, 'answer_aid':answer.aid, 'attention_status':attention_status})
		else:
			return render(request, 'question_show.html', {'qid':qid, 'question_title':question.question_title, 'question_text':question.question_text, 'ask_user_nickname':ask_user.first_name, 'answer_user_nickname':'', 'attention_status':attention_status})
	else:
		return HttpResponseRedirect("/login/")
		
def blog_index_question_show_more(request):
	questions = serializers.serialize("json", Question.objects.all().order_by('?')[:5])
	return HttpResponse(questions, content_type='application/json')
	
def question_show_answer_show_more(request, qid):
	answer=serializers.serialize("json", Answer.objects.filter(answer_question_id=qid).order_by('?')[:3])
	return HttpResponse(answer, content_type='application/json')
	
def answer_show(request, aid):
	if request.user is not None and request.user.is_active:
		if Agree_answer.objects.filter(answer_id=aid, agree_user_id=request.user.id):
			agree_status = 1
		else:
			agree_status = 0		
		answer=Answer.objects.get(aid=aid)
		question=Question.objects.get(qid=answer.answer_question_id)
		answer_user=User.objects.get(id=answer.answer_user_id)
		return render(request, 'answer_show.html', {'aid':aid, 'question_title':question.question_title, 'answer_user_nickname':answer_user.first_name, 'answer_text':answer.answer_text, 'agree_status':agree_status})
	else:
		return HttpResponseRedirect("/login/")
		
def attention_question(request, qid, action):
	if request.user is not None and request.user.is_active:
		if action == '0':
			Attention_question.objects.filter(question_id=qid, attention_user_id=request.user.id).delete()
			attention_dict={'status':'0'}
		elif action == '1':
			Attention_question.objects.create(question_id=qid, attention_user_id=request.user.id)
			attention_dict={'status':'1'}
		attention_dict_json=json.dumps(attention_dict)
		return HttpResponse(attention_dict_json, content_type='application/json')
	else:
		return HttpResponseRedirect('/login/')

def answer_delete(request,aid):
	if request.user is not None and request.user.is_active:
		qid=Answer.objects.get(aid=aid).answer_question_id
		Answer.objects.get(aid=aid).delete()
		return HttpResponseRedirect('/question/'+str(qid)+'/')
	else:
		return HttpResponseRedirect('/login/')

def agree_answer(request, aid, action):
	if request.user is not None and request.user.is_active:
		if action == '0':
			Agree_answer.objects.filter(answer_id=aid, agree_user_id=request.user.id).delete()
			agree_dict={'status':'0'}
		elif action == '1':
			Agree_answer.objects.create(answer_id=aid, agree_user_id=request.user.id)
			agree_dict={'status':'1'}
		agree_dict_json=json.dumps(agree_dict)
		return HttpResponse(agree_dict_json, content_type='application/json')
	else:
		return HttpResponseRedirect('/login/')