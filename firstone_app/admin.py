from django.contrib import admin
from firstone_app import models

admin.site.register(models.Question)
admin.site.register(models.Answer)