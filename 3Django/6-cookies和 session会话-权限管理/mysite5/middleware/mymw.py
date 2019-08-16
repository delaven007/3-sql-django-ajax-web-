
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
class MyMiddleware(MiddlewareMixin):
    '''自定义一个middleware类'''
    count=0    #此变量用来记录整个网站的访问次数
    def process_request(self,request):
        self.__class__.count += 1
        print('count = ',self.__class__.count)
        if self.__class__.count<=5:
            return None
        else:
            return HttpResponse("此网站访问次数已达到上限")

        #return HttpResponseRedirect('/user/login')
        #return None

