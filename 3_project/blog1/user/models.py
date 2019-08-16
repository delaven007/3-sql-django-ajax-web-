from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username=models.CharField(verbose_name='用户名',max_length=50,primary_key=True)
    nickname=models.CharField(verbose_name='昵称',max_length=50)
    e_mail=models.EmailField(verbose_name='E_mail',max_length=50)
    sign=models.CharField(verbose_name='个人签名',max_length=150)
    password=models.CharField(verbose_name='密码',max_length=100)
    info=models.CharField(verbose_name='个人信息',max_length=100)
    avatar=models.ImageField(verbose_name='头像',upload_to='avatar/',null=True)

class Meta():
    db_table='user_profile'

    def __str__(self):
        return "用户名"+self.username+"昵称"+self.nickname+"个性签名"+self.sign
