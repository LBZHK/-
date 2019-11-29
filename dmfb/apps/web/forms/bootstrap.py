from django import forms


class Bootstrap(forms.ModelForm):
    exclude_bootstrap_fields = []
    def __init__(self,*args,**kwwargs):
        super().__init__(*args,**kwwargs)
        for name,field in self.fields.items():
            if name in self.exclude_bootstrap_fields:
                continue
            field.widget.attrs.update({'class':'form-control'})