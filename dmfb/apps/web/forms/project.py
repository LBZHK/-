from django import forms
from .. import models
from .bootstrap import Bootstrap


# 项目modelform
class ProjectModelForm(Bootstrap):
    class Meta:
        model = models.Project
        fields = '__all__'


# 环境modelform
class ProjectEnvModelForm(Bootstrap):
    class Meta:
        model = models.ProjectEnv
        fields = '__all__'