from django.conf.urls import url
from . import views
from django.conf.urls import url
from django.conf.urls import include  # <-- 新导入 include 函数


urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^add$', views.new_book),
    url(r'^list_all', views.list_books),  # <<== 此行是新加的
    url(r'^mod/(\d+)$', views.mod_book_info),
    url(r'^del/(\d+)$', views.del_book),
    url(r'^mod/(\d+)$', views.mod_book_info),
    url(r'^del/(\d+)$', views.del_book),



]