from django.shortcuts import render


def images_view(request):
    return render(request,'show_image.html',locals())

















