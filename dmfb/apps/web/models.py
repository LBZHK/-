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
        return self.env