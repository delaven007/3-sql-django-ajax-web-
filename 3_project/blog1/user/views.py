import hashlib
import json
import time
from tool.login_check import login_check
import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from user.models import UserProfile

@login_check('POST')
def users(request,username=None):
    #注册
    if request.method=='POST':
        json_str=request.body.decode()
        json_obj=json.loads(json_str)
        username=json_obj.get('username')
        e_mail=json_obj.get('e_mail')
        password1=json_obj.get('password1')
        password2=json_obj.get('password2')
        if password1 !=password2:
            result={'code':101,'error':'请确认密码是否相同'}
            return JsonResponse(result)

        really_user=UserProfile.objects.filter(username=username)
        print(1111111111111)
        if really_user:
            result = {'code': 102, 'error': '用户名已存在'}
            return JsonResponse(result)
        p_m=hashlib.sha256()
        p_m.update(password1.encode())

        try:
            UserProfile.objects.create(username=username,e_mail=e_mail,password=p_m.hexdigest())
        except Exception as e:
            print(e)
            result = {'code': 103, 'error': '创建用户失败'}
            return JsonResponse(result)
        token=make_token(username)
        result={'code':200,'username':username,'data':{'token':token.decode()}}
        return JsonResponse(result)



def make_token(username, expir=86400):
    """
    生成token
    :param username:
    :param expir:
    :return:
    """
    key = '1234567abcdef'
    now_t = time.time()
    data = {'username': username, 'exp': int(now_t + expir)}
    return jwt.encode(data, key, algorithm='HS256')









