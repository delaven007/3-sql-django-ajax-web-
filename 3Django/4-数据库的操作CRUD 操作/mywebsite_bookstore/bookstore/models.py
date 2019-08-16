from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title=models.CharField("书名",max_length=50,default='untitled')
    pub=models.CharField("出版社",max_length=50,default="")
    price=models.DecimalField("价格",max_digits=7,decimal_places=2,default="0.0")
    market_price=models.DecimalField("市场价",max_digits=7,decimal_places=2,default="0.0")










