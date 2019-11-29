from django.template import Library

register = Library()

@register.simple_tag
def un_deploy_num(projectenv):
    total = projectenv.deploytask_set.all().count()
    un_deploy = projectenv.deploytask_set.filter(status=1).count()
    msg = "%s/%s"%(un_deploy,total)
    return msg


