from django.db import models

# Create your models here.

class Users(models.Model):
    uname=models.CharField('用户名',max_length=30)
    upwd=models.CharField('密码',max_length=50)
    uemail=models.EmailField('电子邮箱',max_length=50)
    nickname=models.CharField('昵称',max_length=30)

    def __str__(self):
        return "用户名"+self.uname,'昵称'+self.nickname

















