from django.contrib import admin

# Register your models here.
#one2many/admin

from . import models

admin.site.register(models.Publisher)
admin.site.register(models.Book2)


