import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

from user.models import UserProfile

def tokens(request):
    '''
    创建token==登录
    :param request:
    :return:
    '''
    #登录
    # 前端访问地址：http://127.0.0.1:5000/login
    if not request.method == 'POST':
        result = {'code': 102, 'error': 'Please use POST!!'}

        return JsonResponse(result)
    json_str = request.body
    if not json_str:
        result = {'code': 103, 'error': 'Please give me json'}
        return JsonResponse(result)
    json_obj = json.loads(json_str)
    username = json_obj.get('username')
    password = json_obj.get('password')
    if not username:
        result = {'code': 104, 'error': 'Please give username!'}
        return JsonResponse(result)
    if not password:
        result = {'code': 105, 'error': 'Please give password!'}
        return JsonResponse(result)
    users = UserProfile.objects.filter(username=username)
    if not users:
        result = {'code': 106, "error": 'The username or password is wrong!'}
        return JsonResponse(result)
    # 生成密码哈希
    p_m = hashlib.sha256()
    p_m.update(password.encode())
    if users[0].password != p_m.hexdigest():  # 把二进制哈希密码转换成16进制密码
        result = {'code': 107, 'error': 'The username or password is wrong!'}
        return JsonResponse(result)
    # 生成token
    token = make_token(username)
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
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
