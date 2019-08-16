import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .models import Users


def create_view(request):
    return render(request,'01-createxhr.html')

def server02_views(request):
    return HttpResponse("这是server02的响应内容")

def ajaxget_views(request):
    return render(request,'02-ajax-get.html')

def getparams_views(request):
    return render(request,'03-ajax-get-params.html')

def server03_views(request):
    #接收参数
    name=request.GET['name']
    age=request.GET['age']
    #相应数据给前端
    s='姓名：%s,年龄：%s'%(name,age)
    return HttpResponse(s)

def register_views(request):
    return render(request,'04-register.html')

def checkuname_views(request):
    #1.接收前端传递过来的参数  -uname
    uname = request.GET['uname']
    #2.判断uname在Users实体中是否存在[查询操作]
    users=Users.objects.filter(uname=uname)
    #3.根据查询结果，给出响应
    if users:
        return HttpResponse("1")
    return HttpResponse("0")

def reguser_views(request):
    #1.接收数据
    uname=request.GET['uname']
    upwd=request.GET["upwd"]
    uemail=request.GET["uemail"]
    nickname=request.GET["nickname"]
    #2.通过实体类实现增加(通过异常处理增加失败问题)
    try:
        Users.objects.create(uname=uname,upwd=upwd,
                         uemail=uemail,nickname=nickname)
        return  HttpResponse("1")
    except Exception as ex:
        print(ex)
        return HttpResponse("0")

def regpost_views(request):
    uname = request.POST['uname']
    upwd = request.POST["upwd"]
    uemail = request.POST["uemail"]
    nickname = request.POST["nickname"]
    # 2.通过实体类实现增加(通过异常处理增加失败问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd,
                             uemail=uemail, nickname=nickname)
        return HttpResponse("1")
    except Exception as ex:
        print(ex)
        return HttpResponse("0")


def post_views(request):
    return render(request,"05-post.html")

def server05_views(request):
    uname=request.POST["uname"]
    upwd=request.POST["upwd"]
    msg="用户名:%s,密码:%s"%(uname,upwd)
    return HttpResponse(msg)

def users_views(request):
    return render(request,'06-ajax-users.html')

def server06_views(request):
    users=Users.objects.all()
    msg=""
    for u in users:
        msg+="%s_%s_%s_%s_%s|"%(u.id,u.uname,u.upwd,u.uemail,u.nickname)
    msg=msg[0:-1]    #最后一个|被切走
    return HttpResponse(msg)


def json_views(request):
    return render(request,"07-jason.html")

def jsonserver_views(request):
    #1.使用字典表示json数据
    dic={
        'course':'ajax',
        'duration':'3',
        'place':'1904',
    }
    list1=[{'system':'computer','class':'1904','number':'54'},
           {'system': 'UI', 'class': '1804', 'number': '53'},
           {'system': 'UIC', 'class': '1901', 'number': '44'},
           ]
    #2.将dic通过json.dumps装换成json格式字符串
    jsonstr1=json.dumps(list1)
    jsonstr = json.dumps(dic)
    return HttpResponse(jsonstr1)
from django.core import serializers
                        #序列化器
#queryset不支持json
def jsonusers_views(request):
    users = Users.objects.all()
    jsonUsers=serializers.serialize('json',users)
    return HttpResponse(jsonUsers)

def jsonserver10_views(request):
    users=Users.objects.all()
    jsonUsers=serializers.serialize('json',users)
    return HttpResponse(jsonUsers)

def jsonusers10_views(request):
    return render(request, '10-json-users.html')

def front_views(request):
    return render(request,'11-front-json.html')

def serverjson_views(request):
    jsonstr='{"uname":"wangwc","uage":30,"ugender":"unknown"}'
    #通过json.loads()将jsonstr转换为python字典
    dic=json.loads(jsonstr)
    str1="姓名:%s,年龄:%s,性别:%s"%(dic['uname'],dic['uage'],dic['ugender'])
    return HttpResponse(str1)

def server12_views(request):
    params=request.GET['params']
    #将params转换成pyhton字典
    dic=json.loads(params)
    try:
        Users.objects.create(uname=dic['uname'],upwd=dic['upwd'],uemail=dic['uemail'],nickname=dic['nickname'])
        return HttpResponse("注册成功")
    except Exception as e:
        print(e)
        return HttpResponse('注册失败')
def register12_views(request):
    return render(request, '12-register-json.html')
def head_views(request):
    return render(request,'13-head.html')


def index_views(request):
    return render(request,'13-index.html')

def jqget_views(request):
    return render(request,'14-jq-get.html')

def search_views(request):
    return render(request,'15-onkeyup.html')

def server15_views(request):
    #1.接受前端传递参数        -kw
    kw = request.GET['kw']
    #2.查询Users中uname列包含kw信息
    users=Users.objects.filter(uname__contains=kw)
    #3.将uname封装成列表再转换成JSON串响应
    uList=[]
    if users:
        for u in users:
            uList.append(u.uname)
    return HttpResponse(json.dumps(uList))


def jqajax_views(request):
    return render(request,'16-jq-ajax.html')
















