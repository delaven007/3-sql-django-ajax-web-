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






