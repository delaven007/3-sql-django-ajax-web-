from django.db import models

# Create your models here.
#user/model.py

class User(models.Model):
    username=models.CharField("用户名",max_length=30)
    password=models.CharField("密码",max_length=50)


    def __str__(self):
        return "用户名" + self.username




