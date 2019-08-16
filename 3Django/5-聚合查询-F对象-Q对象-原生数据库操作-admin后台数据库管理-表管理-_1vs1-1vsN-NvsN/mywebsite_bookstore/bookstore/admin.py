from django.contrib import admin

# Register your models here.
from . import models

class BookManager(admin.ModelAdmin):    #编写模型管理器类
    list_display = ['id','title','pub_house','price','market_price']
    list_display_links = ['id','title','price']
    list_filter = ['pub_house']
    search_fields = ['title','pub_house','price']
    list_editable = ['pub_house','market_price']
    pass

admin.site.register(models.Book,BookManager)
#admin.site.register(models.Author)
admin.site.register(models.Wife)




















