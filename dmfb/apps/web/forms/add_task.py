from .bootstrap import Bootstrap
from .. import models

class DeployTaskModelForm(Bootstrap):
    class Meta:
        model = models.DeployTask
        # fields = '__all__'
        exclude = ['uid','status','env']