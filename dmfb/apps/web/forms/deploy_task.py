from .bootstrap import Bootstrap
from .. import models

class DeployTaskModelForm(Bootstrap):
    class Meta:
        model = models.DeployTask
        # fields = '__all__'
        exclude = ['uid', 'status', 'env']

    def clean(self):
        tag = self.cleaned_data.get('tag')
        branch = self.cleaned_data.get('branch')
        commit = self.cleaned_data.get('commit')
        if tag:
            return self.cleaned_data
        if branch or commit:
            return self.cleaned_data
        self.add_error('tag','tag或branch任选其一')
