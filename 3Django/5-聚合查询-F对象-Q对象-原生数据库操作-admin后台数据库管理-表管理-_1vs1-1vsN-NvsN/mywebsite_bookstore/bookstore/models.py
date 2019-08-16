from django.db import models

# Create your models here.

from django.db import models


class Book(models.Model):
    title = models.CharField("书名:", max_length=50, default="untitled")
    pub_house = models.CharField("出版社:", max_length=100, default='')
    price = models.DecimalField('定价:', max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField('零售价:', max_digits=7, decimal_places=2, default=9999)
    def __str__(self):
        return "---书名:--->" + self.title + "-----出版社--->" + self.pub_house
class Author(models.Model):
    name=models.CharField("姓名",unique=True,db_index=True,max_length=30)
    age=models.IntegerField("年龄")


class Wife(models.Model):
    name=models.CharField("姓名",max_length = 15)
    author=models.OneToOneField(Author)
    def __str__(self):
        return "作家妻子:"+self.name


