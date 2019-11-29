"""dmfb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import project,rsa,server,deploy

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^rsa/$', rsa.rsa,name='rsa'),
    url(r'^add/rsa/$', rsa.add_rsa,name='add_rsa'),
    url(r'^del/rsa/(\d+)/$', rsa.del_rsa,name='del_rsa'),
    url(r'^edit/rsa/(\d+)/$', rsa.edit_rsa,name='edit_rsa'),

    url(r'^server/$', server.server, name='server'),
    url(r'^add/server/$', server.add_server, name='add_server'),
    url(r'^del/server/(\d+)/$', server.del_server, name='del_server'),
    url(r'^edit/server/(\d+)/$', server.edit_server, name='edit_server'),

    url(r'^project/$', project.project, name='project'),
    url(r'^add/project/$', project.add_project, name='add_project'),
    url(r'^del/project/(\d+)/$', project.del_project, name='del_project'),
    url(r'^edit/project/(\d+)/$', project.edit_project, name='edit_project'),

    url(r'^projectenv/$', project.projectenv, name='projectenv'),
    url(r'^add/projectenv/$', project.add_projectenv, name='add_projectenv'),
    url(r'^del/projectenv/(\d+)/$', project.del_projectenv, name='del_projectenv'),
    url(r'^edit/projectenv/(\d+)/$', project.edit_projectenv, name='edit_projectenv'),

    url(r'^deploy/(?P<env_id>\d+)/$', deploy.deploy, name='deploy'),
    url(r'^add/deploy/(?P<env_id>\d+)/$', deploy.add_deploy, name='add_deploy'),
    url(r'^del/deploy/(\d+)/$', deploy.del_deploy, name='del_deploy'),
    url(r'^edit/deploy/(\d+)/$', deploy.edit_deploy, name='edit_deploy'),

]
