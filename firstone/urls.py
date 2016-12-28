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

urlpatterns = [
    url(r'^index/', firstone_app_views.index, name='home'),
    url(r'^login/', firstone_app_views.login, name='login'),
    url(r'^signup/', firstone_app_views.signup, name='signup'),
    url(r'^logout/', firstone_app_views.logout, name='logout'),
    url(r'^userpage/', firstone_app_views.userpage, name='userpage'),
    url(r'^blog_index/', firstone_app_views.blog_index, name='blog_index'),
	url(r'^question_update/', firstone_app_views.question_update, name='question_update'),
	url(r'^question/(\d+)/$', firstone_app_views.question_show, name='question_show'),
	url(r'^blog_index_question_show_more/$', firstone_app_views.blog_index_question_show_more, name='blog_index_question_show_more'),
    url(r'^admin/', admin.site.urls),
]
