from django.conf.urls import url
from . import views
urlpatterns = [
    #演示创建xhr
    url(r'^01-createXhr/',views.create_view),
    #使用ajax发送get请求的步骤
    url(r'02-server/$',views.server02_views),
    url(r'02-ajax-get/$',views.ajaxget_views),
    #使用ajax发送get请求并附带参数
    url(r'03-ajax-get-params/$',views.getparams_views),
    url(r'^03-server/$',views.server03_views),
    #
    url(r'04-checkuname/$',views.checkuname_views),
    url(r'^04-register/$',views.register_views),

    url(r"^add_date/",views.add_date_views),









]