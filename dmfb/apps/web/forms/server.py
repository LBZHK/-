from django import forms
from .. import models
from .bootstrap import Bootstrap

# 服务器modelform
class ServerModelForm(Bootstrap):
    class Meta:
        model = models.Server
        fields = '__all__'
