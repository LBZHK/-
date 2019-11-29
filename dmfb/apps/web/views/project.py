from django.shortcuts import render,HttpResponse,redirect
from .. import models
from ..forms.project import ProjectEnvModelForm, ProjectModelForm
from django.http import JsonResponse


# 项目展示
def project(request):
    all_project = models.Project.objects.filter()
    return render(request,'web/project.html',{'all_project':all_project})

# 项目添加
def add_project(request):
    if request.method == 'GET':
        form_obj = ProjectModelForm()
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ProjectModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('project')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})

# 项目删除
def del_project(request,id):
    models.Project.objects.filter(pk=id).delete()
    return JsonResponse({'status':True})

# 项目编辑
def edit_project(request,id):
    form_obj = models.Project.objects.filter(pk=id).first()
    if request.method == 'GET':
        form_obj = ProjectModelForm(instance=form_obj)
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ProjectModelForm(request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('project')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})


# 环境展示
def projectenv(request):
    all_projectenv = models.ProjectEnv.objects.filter()
    return render(request,'web/projectenv.html',{'all_projectenv':all_projectenv})

# 环境添加
def add_projectenv(request):
    if request.method == 'GET':
        form_obj = ProjectEnvModelForm()
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ProjectEnvModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('projectenv')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})

# 环境删除
def del_projectenv(request,id):
    models.ProjectEnv.objects.filter(pk=id).delete()
    return JsonResponse({'status': True})

# 环境编辑
def edit_projectenv(request,id):
    form_obj = models.ProjectEnv.objects.filter(pk=id).first()
    if request.method == 'GET':
        form_obj = ProjectEnvModelForm(instance=form_obj)
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = ProjectEnvModelForm(request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('projectenv')
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})