from django.db import models
from user import models as user_models
# Create your models here.


class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间',
                                       auto_now_add=True)
    mod_time = models.DateTimeField('修改时间',
                                    auto_now=True)
    user = models.ForeignKey(user_models.User)


    def __str__(self):
        return "标题"+self.title






