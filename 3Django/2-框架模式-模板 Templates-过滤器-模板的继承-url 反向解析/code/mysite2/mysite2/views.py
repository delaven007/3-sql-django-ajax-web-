# file/mysite2/view.py

from django.http import HttpResponse
# 1
from django.template import loader
# 2
from django.shortcuts import render

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/text_post" method="post">
    <input type="text" name="search_name">
    <input type="submit" value="开始搜索">
</form>

</body>
</html>
"""


def text_post_view(request):
    if request.method == 'GET':
        return HttpResponse(html)
    if request.method == 'POST':
        value = request.POST['search_name']
        return HttpResponse("search_name=" + value)


# def text1_view(request):
# #way1.
# #t绑定模块对象
# t = loader.get_template("myhomepage.html")
# #用模板生成html
# html=t.render()
# #返回给浏览器
# return HttpResponse(html)

# way2
def text1_view(request):
    person = {
        'name': 'tedu',
        'age': 19,
    }
    return render(request, "myhomepage.html", person)


def mypage2_view(request):
    myvar = 999
    mystr = "hello kitty"
    city = ['北京', '上海', '深圳', '珠海']
    person = {
        'name': 'tarena',
        'age': 20,
    }
    money = 999999999

    def myfun1():
        return "函数结果!!!"

    return render(request, 'mypage2.html', locals())

    # return render(request,'mypage2.html',{'myvar':myvar},mystr,mylist,)


def page1_view(request):
    return render(request, 'page1.html')


def page2_view(request):
    return render(request, 'page2.html')


def page0_view(request):
    return render(request, 'mybase.html')


def page3_view(request):
    return render(request, 'page3.html')


def pagen_view(request, n):
    return render(request, 'pagen.html', locals())
