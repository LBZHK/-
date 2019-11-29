from django.shortcuts import render,HttpResponse,redirect
from .. import models
from ..forms.server import ServerModelForm
from django.http import JsonResponse


# 服务器展示
def server(request):
    all_server = models.Server.objects.filter()
    return render(request,'web/server.html',{'all_server':all_server})

# 服务器添加
def add_server(request):
    if request.method == 'GET':
        form_obj = ServerModelForm()
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ServerModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('server')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})

# 服务器删除
def del_server(request,id):
    models.Server.objects.filter(pk=id).delete()
    return JsonResponse({'status':True})

# 服务器编辑
def edit_server(request,id):
    form_obj = models.Server.objects.filter(pk=id).first()
    if request.method == 'GET':
        form_obj = ServerModelForm(instance=form_obj)
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ServerModelForm(request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('server')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})
