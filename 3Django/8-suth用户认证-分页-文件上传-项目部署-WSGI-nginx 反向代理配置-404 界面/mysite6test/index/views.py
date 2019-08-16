from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
# Create your views here.
#note/view

def index_view(request):
    return render(request,'index/index.html',locals())

def upload_view(request):
    if request.method == 'GET':
       return render(request,'index/upload_file.html',locals())
    elif request.method == 'POST':
        #此时可以通过request.files获取上传文件
        a_file=request.FILES['myfile']
        # 保存上传的文件到mysite5/static/files+
        #得到要保存的文件路径
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename ,"wb") as f:
            #a_file 绑定一个文件流对象
            data=a_file.file.read()
            f.write(data)
        return HttpResponse('文件'+ a_file.name+'上传成功')
















