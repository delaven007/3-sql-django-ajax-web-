from django.http import HttpResponse

def birthday_view(request):
    html="生日为:"
    if request.method == 'GET':
        year=request.GET['year']
        month=request.GET['month']
        day=request.GET['day']
        html+=year+'年'+ month +'月'+ day +'日'
    return HttpResponse(html)

def sum_view(request):
    html="页面显示结果:"
    if request.method == 'GET':
        start=request.GET.get('start','0')
        stop=request.GET['stop']
        step=request.GET['step']
        html+=str(sum(range(int(start),int(stop),int(step))))

    return HttpResponse(html)
def page_view(request):
    html = ''
    if request.method == 'GET':
        dic = dict(request.GET)
        s = str(dic)
        html += 'GET请求:' + s
        # b = request.GET['b']
        b = request.GET.get('b', '没有值')
        a = request.GET.getlist('a')
        html += "<br> b=" + b
        html += "<br> a=" + str(a)
    elif request.method == 'POST':
        pass
    return HttpResponse(html)


def show_info_view(request):
    html = '<h1>request.path</h1>'
    if request.method == 'GET':
        html += "<h1>正在get请求</h1>"
    if request.method == 'POST':
        html += "<h1>正在post请求</h1>"
    html += "<h3>您的IP地址是：+request.META['REMOTE_ADDR']</h3>"
    html += "META="
    return HttpResponse(html)


def page1_view(request):
    html = "这是编号为1的网页"
    html += '<a href="http://www.tmooc.cn">达内</a>'
    html += '<a href="/">返回首页</a>'
    return HttpResponse(html)


def page2_view(request):
    html = "这是编号为2的网页"
    html += '<a href="http://www.tmooc.cn">达内</a>'
    html += '<a href="/">返回首页</a>'
    return HttpResponse(html)


def index_view(request):
    html = "这是我的首页"
    html += "跳转到page1-->" + "<a href='/page1'>page1</a>"
    html += "跳转到page2-->" + "<a href='/page2'>page2</a>"

    return HttpResponse(html)


def year_view(request, y):
    html = "URL中的年份是:" + y
    return HttpResponse(html)


def date_view(request, y, m, d):
    """y,m,d绑定年月日"""
    html = y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def jishu_view(request, x, y, z):
    html = "页面显示结果:"
    if y == 'add':
        return HttpResponse(html + str(int(x) + int(z)))
    elif y == 'sub':
        return HttpResponse(html + str(int(x) - int(z)))
    elif y == 'mul':
        return HttpResponse(html + str(int(x) * int(z)))
    else:
        return HttpResponse('不能运算')
