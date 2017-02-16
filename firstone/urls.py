"""firstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstone_app import views as firstone_app_views
from diary import views as diary_views

urlpatterns = [
    url(r'^welcome/', firstone_app_views.index, name='welcome'),
    url(r'^login/', firstone_app_views.login, name='login'),
    url(r'^signup/', firstone_app_views.signup, name='signup'),
    url(r'^logout/', firstone_app_views.logout, name='logout'),
    url(r'^userpage/', firstone_app_views.userpage, name='userpage'),
    url(r'^index/(\d+)/$', firstone_app_views.blog_index, name='index'),
	url(r'^question_update/', firstone_app_views.question_update, name='question_update'),
	url(r'^question/(\d+)/$', firstone_app_views.question_show, name='question_show'),
	url(r'^question_show_more/$', firstone_app_views.blog_index_question_show_more, name='question_show_more'),
	url(r'^question_show_answer_show_more/(\d+)/$', firstone_app_views.question_show_answer_show_more, name='question_show_answer_show_more'),
	url(r'^answer/(\d+)/$', firstone_app_views.answer_show, name='answer_show'),
	url(r'^attention_question/(\d+)/(\d+)/$', firstone_app_views.attention_question, name='attention_question'),
    url(r'^answer_delete/(\d+)/$', firstone_app_views.answer_delete, name='answer_delete'),
    url(r'^answer_agree/(\d+)/(\d+)/$', firstone_app_views.agree_answer, name='agree_answer'),
    url(r'^diary/', diary_views.home, name='diary_home'),
    url(r'^create_diary/([\u4e00-\u9fa5]+)/(.+)/(.+)/(.+)/$', diary_views.create_diary, name='create_diary'),
    url(r'^admin/', admin.site.urls),
]
