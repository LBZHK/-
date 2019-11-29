from django.shortcuts import render,HttpResponse,redirect
from .. import models
from ..forms.rsa import RsaModelForm
from django.http import JsonResponse



# 私钥展示
def rsa(request):
    all_rsa = models.Rsa.objects.filter()
    return render(request,'web/rsa.html',{'all_rsa':all_rsa})

# 私钥添加
def add_rsa(request):
    if request.method == 'GET':
        form_obj = RsaModelForm()
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = RsaModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('rsa')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})

# 私钥删除
def del_rsa(request,id):
    models.Rsa.objects.filter(pk=id).delete()
    return JsonResponse({'status':True})

# 私钥编辑
def edit_rsa(request,id):
    form_obj = models.Rsa.objects.filter(pk=id).first()
    if request.method == 'GET':
        form_obj = RsaModelForm(instance=form_obj)
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = RsaModelForm(request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('rsa')
        else:
            return render(request, 'web/form.html', {'rsa_obj': form_obj})