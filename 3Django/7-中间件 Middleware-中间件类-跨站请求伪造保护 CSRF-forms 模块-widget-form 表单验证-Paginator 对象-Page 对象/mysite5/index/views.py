from django.shortcuts import render

# Create your views here.
#note/view

def index_view(request):
    return render(request,'index/index.html',locals())
















