import jwt
from django.http import JsonResponse

from user.models import UserProfile

token_key='1234567abcdef'
def login_check(*methods):
    def _login_check(func):
        def wrapper(request,*args,**kwargs):
            token=request.META.get('HTTP_AUTHORIZATION')
            if not methods:
                #如果当前没传任何参数，则直接返回视图函数
                return func(request,*args,**kwargs)
            else:
                #如果传参，检查request.method是否在参数列表中
                if request.method not in methods:
                    return func(request,*args,**kwargs)
            if not token:
                result={'code':'109','error':'Please give me token!!'}
                return JsonResponse(result)

            try:
                res=jwt.decode(token,token_key)
                print(res)
            except Exception as e:

                print(e)
                result={'code':'108','error':'The token is wrong!!!'}
                return JsonResponse(result)
            #token校验成功

            username=res['username']
            try:
                user=UserProfile.objects.get(
                username=username
                )
            except:
                user=None
            if not user:

                result = {'code': '110', 'error': 'The user is existed!!!'}
                return JsonResponse(result)
            #将user赋值给给request对象
            request.user=user


            return func(request,*args,**kwargs)
        return wrapper
    return _login_check

def get_user_by_request(request):
    token=request.Meta.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res=jwt.decode(token,token_key)
    except:
        return None
    if not res:
        return None
    username=res['username']
    try:
        user=UserProfile.objects.get(username=username)
    except:
        return None

    if not user:
        return None
    return user

