from django import forms
from .. import models
from .bootstrap import Bootstrap


# 私钥modelform
class RsaModelForm(Bootstrap):
    class Meta:
        model = models.Rsa
        fields = '__all__'
