
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^add',views.add_view),
    url(r'^$',views.list_view),
    url(r'^mod/(\d+)',views.mod_view),  #(\d+):提取id
    url(r'^del/(\d+)',views.del_view),



]
















