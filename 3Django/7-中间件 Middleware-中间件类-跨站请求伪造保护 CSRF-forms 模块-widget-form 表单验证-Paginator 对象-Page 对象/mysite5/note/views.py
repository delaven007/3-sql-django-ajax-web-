from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect
from user.models import User
# Create your views here.

#写一个函数装饰器,检查用户是否登录
#如果没有登录，跳转到登录页面
def check_login(fn):
    def warp(request,*args,**kwargs):
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        else:
            return fn(request,*args,**kwargs)
    return warp

def add_view(request):
    #检查用户是否登录，如果没有,进入登录页面
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')

    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method =="POST":
        #根据登录用户的id找到此用户
        try:
            a_user=User.objects.get(id=request.session['user']['id'])
        except:
            return HttpResponse("登录用户数据错误")

        title=request.POST.get('title','')
        content=request.POST.get('content','')
        #根据表单内容创建记录
        models.Note.objects.create(
            title=title,
            content=content,
            user=a_user,
        )
    return HttpResponseRedirect('/note')

@check_login
def list_view(request):
    try:
        a_user_id=request.session['user']['id']
        a_user=User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    notes=a_user.note_set.all()     #获取当前用户的所有笔记
    return render(request,'note/list_note.html',locals())

@check_login
def del_view(request,id):
    #先得到当前用户信息
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    #根据用户和id找到对应笔记
    a_note=a_user.note_set.get(id=id)
    a_note.delete()  #删除
    return HttpResponseRedirect('/note/')


@check_login
def mod_view(request,id):
    # 先得到当前用户信息
    try:
        a_user_id = request.session['user']['id']
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse('失败')
    # 根据用户和id找到对应笔记
    a_note = a_user.note_set.get(id=id)
    if request.method=='GET':
        return render(request,'note/mod_note.html',locals())
    elif request.method=="POST":
        #从表单提取数据
        title=request.POST.get('title',"")
        content=request.POST.get('content','')
        #修改数据
        a_note.title=title
        a_note.content=content
        a_note.save()
        return HttpResponseRedirect('/note/')



















