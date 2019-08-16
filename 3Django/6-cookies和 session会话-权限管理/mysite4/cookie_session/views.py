from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def set_cookie(request):
    # 1.
    resp= HttpResponse("哦了")
    resp.set_cookie('aaa','bbb')
    return resp

    #2.

def get_cookie(request):
    #得到浏览器aaa 对应的值
    dic = request.COOKIES['aaa']
    v = str(dic)
    print(v)

    dic=request.COOKIES
    s=str(dic)




    return HttpResponse(s)







