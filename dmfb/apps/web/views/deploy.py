import uuid

from django.shortcuts import render,HttpResponse,redirect
from .. import models
from ..forms.deploy_task import DeployTaskModelForm
from django.http import JsonResponse
from django.urls import reverse


# 任务展示
def deploy(request,env_id):
    env_obj = models.ProjectEnv.objects.filter(id=env_id).first()
    all_deploy = models.DeployTask.objects.filter(env=env_obj)
    return render(request,'web/deploy.html',{'all_deploy':all_deploy,'env_obj':env_obj})

# 任务添加
def add_deploy(request,env_id):
    if request.method == 'GET':
        env_obj = models.ProjectEnv.objects.filter(id=env_id).first()
        servers_obj = env_obj.servers.all()
        project = env_obj.project
        return render(request,'web/add_task.html',{'env_obj':env_obj,'servers_obj':servers_obj,'project':project})

        # form_obj = DeployTaskModelForm()
        # return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        tag = request.POST.get('tag')
        branch = request.POST.get('branch')
        commit = request.POST.get('commit')
        models.DeployTask.objects.create(
            uid=str(uuid.uuid4()),
            status = 1,
            env_id=env_id,
            tag=tag,
            branch=branch,
            commit=commit,
        )
        return redirect(reverse('deploy', kwargs={'env_id': env_id}))


        # form_obj = DeployTaskModelForm(request.POST)
        # if form_obj.is_valid():
        #     form_obj.instance.uid=str(uuid.uuid4())
        #     form_obj.instance.status=1
        #     form_obj.instance.env_id=env_id
        #     form_obj.save()
        #     return redirect(reverse('deploy', kwargs={'env_id':env_id}))
        # else:
        #     return render(request, 'web/form.html', {'form_obj': form_obj})

# 任务删除
def del_deploy(request,env_id):
    models.DeployTask.objects.filter(pk=env_id).delete()
    return JsonResponse({'status':True})

# 任务编辑
def edit_deploy(request,id):
    form_obj = models.DeployTask.objects.filter(pk=id).first()

    if request.method == 'GET':
        form_obj = DeployTaskModelForm(instance=form_obj)
        return render(request,'web/form.html',{'form_obj':form_obj})
    else:
        form_obj = DeployTaskModelForm(request.POST,instance=form_obj)
        if form_obj.is_valid():
            form_obj.save()
            form_obj = models.DeployTask.objects.filter(pk=id).first()
            return redirect(reverse('deploy', kwargs={'env_id':form_obj.env.id}))
        else:
            return render(request, 'web/form.html', {'form_obj': form_obj})


