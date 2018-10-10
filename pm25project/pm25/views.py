from django.shortcuts import render,get_object_or_404
from . models import pm25
from .forms import Pm25_Form
from pm25project.ip_api import main



def home(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    # else:
    #     ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
    ip = ''
    city_name = main(ip)
    city_name_ip = pm25.objects.filter(city_name__contains=city_name)

    if not city_name_ip:
        city_name_ip = pm25.objects.filter(city_name='北京')

    return render(request, 'home.html', {
        'city_name_ip':city_name_ip[0],
    })



def pm25s(request):
    if request.method == 'POST':
        pm25_form = Pm25_Form(request.POST)
        if pm25_form.is_valid():
            city = request.POST.get('city','')
            try:
                pm25_info = pm25.objects.get(city_name=city)
            except:
                return render(request, 'pm25.html', {
                    'Pm25_Form': pm25_form,
                    'error_msg': "请输入有效的城市名",
                })

            return render(request, 'pm25.html', {
                'pm25_info':pm25_info,
            })

        else:
            return render(request, 'pm25.html', {
                'Pm25_Form': pm25_form,
                'error_msg': "请输入有效的城市名",
            })


    elif request.method == 'get':
        pm25_form = Pm25_Form()
        return render(request,'home.html',{
            'Pm25_Form':pm25_form,
        })

def delete(request):
    pm25.objects.all().delete()
    return render(request,'delete.html',{
        "msg":"删除成功"
    })

def dw(request):

    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    # else:
    #     ip = request.META.get('REMOTE_ADDR')#这里获得代理ip

    ip = '27.37.77.82'
    city_name = main(ip)

    city_name_ip = pm25.objects.filter(city_name__contains=city_name)

    if not city_name_ip:
        return render(request, 'delete.html', {
            "msg":"none"
        })

    return render(request, 'delete.html', {
        'city_name_ip':city_name_ip[0]
    })

