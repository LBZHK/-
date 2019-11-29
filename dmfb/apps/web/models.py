from django.db import models


class Rsa(models.Model):
    status_choices = (
        (1, '启用'),
        (2, '停用'),
    )
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=status_choices)
    private_key = models.TextField(verbose_name='私钥')

class Server(models.Model):
    hostname = models.CharField(verbose_name='主机名', max_length=32)

    def __str__(self):
        return self.hostname

class Project(models.Model):
    title = models.CharField(verbose_name='项目名', max_length=32)
    repo = models.URLField(verbose_name='git仓库地址')

    def __str__(self):
        return self.title

class ProjectEnv(models.Model):
    project = models.ForeignKey(verbose_name='项目', to='Project')
    env_choices = (
        (1, '测试'),
        (2, '正式')
    )
    env = models.IntegerField(verbose_name='环境', choices=env_choices)
    path = models.CharField(verbose_name='线上部署路径', max_length=128)
    servers = models.ManyToManyField(verbose_name='服务器', to='Server')

    def __str__(self):
        return "%s(%s)"%(self.project, self.get_env_display())


class DeployTask(models.Model):
    uid = models.CharField(verbose_name='任务ID', max_length=64,help_text="任务ID格式为：项目-版本-时间，例如 cmdb-v1-201911012359.zip")
    status_choices = (
        (1, '待发布'),
        (2, '发布中'),
        (3, '成功'),
        (4, '失败'),
    )
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=status_choices, default=1)

    env = models.ForeignKey(verbose_name='环境', to='ProjectEnv')

    # 正式发布用tag
    tag = models.CharField(verbose_name='版本', max_length=32,null=True,blank=True)

    # 测试发布用branch 、commit
    branch = models.CharField(verbose_name='分支', max_length=32,null=True,blank=True)
    commit = models.CharField(verbose_name='提交记录', max_length=40,null=True,blank=True)


class DeployServer(models.Model):
    """
    上线记录
    """
    deploy = models.ForeignKey(verbose_name='部署', to='DeployTask')
    server = models.ForeignKey(verbose_name='服务器', to='Server')
    status_choices = (
        (1, '发布中'),
        (2, '失败'),
        (3, '成功'),
    )
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=status_choices)