from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
# user/views

def login_view(request):
    # value=request.session.get('mypassword','None')
    # print('密码是:',value)

    if request.method == "GET":
        username = request.COOKIES.get('myname', '')
        return render(request, 'user/login.html', locals())
    elif request.method == "POST":
        username = request.POST.get('username', '')
        # 表单验证（验证用户提交的数据是否合法）
        if username == "":
            name_error = '请填写用户名!!'
            return render(request, 'user/login.html', locals())

        password = request.POST.get("password", "")
        #用session保存密码
        # request.session['mypassword']=password

        remember = request.POST.get('remember', '')
        #进行登录逻辑操作
        try:
            auser=models.User.objects.get(
                username=username,password=password
            )
        except:
            password_error="用户名和密码不正确!"
            return render(request,'user/login.html',locals())
        #如果走到此处，证明用户名密码正确,在session里标识用户是登录状态
        request.session['user']={
            'name':auser.username,
            'id':auser.id,
        }

        # resp = HttpResponse('提交成功:remember:' + remember)
        resp= HttpResponseRedirect('/')
        if remember == '1':
            resp.set_cookie('myname', username, max_age=365*24*60*60)
        else:
            resp.delete_cookie('myname')
        return resp
def logout_view(request):
    if 'user'in request.session:
        del request.session['user']
    #返回到主页
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/')

from . import forms

def reg2_view(request):
    if request.method=="GET":
        reg2=forms.Reg2()
        return render(request,'user/reg2.html',locals())

    elif request.method =="POST":
        #way1.    request.POST

        #way2
        form =forms.Reg2(request.POST)
        if form.is_valid():                   #表单验证
            html=str(form.cleaned_data)       #干净的数据
            return HttpResponse(html)
        else:
            return HttpResponse("您提交的数据不合法")













