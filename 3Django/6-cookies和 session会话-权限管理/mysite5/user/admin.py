from django.contrib import admin

# Register your models here.

from . import models


#让后台管理操作模型类
admin.site.register(models.User)
















