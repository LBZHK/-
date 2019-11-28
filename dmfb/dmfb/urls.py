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
from apps.web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^petch/code/$', views.petch_code),

    url(r'^rsa/$', views.rsa,name='rsa'),
    url(r'^add/rsa/$', views.add_rsa,name='add_rsa'),
    url(r'^del/rsa/(\d+)/$', views.del_rsa,name='del_rsa'),
    url(r'^edit/rsa/(\d+)/$', views.edit_rsa,name='edit_rsa'),

    url(r'^server/$', views.server, name='server'),
    url(r'^add/server/$', views.add_server, name='add_server'),
    url(r'^del/server/(\d+)/$', views.del_server, name='del_server'),
    url(r'^edit/server/(\d+)/$', views.edit_server, name='edit_server'),

    url(r'^project/$', views.project, name='project'),
    url(r'^add/project/$', views.add_project, name='add_project'),
    url(r'^del/project/(\d+)/$', views.del_project, name='del_project'),
    url(r'^edit/project/(\d+)/$', views.edit_project, name='edit_project'),

    url(r'^projectenv/$', views.projectenv, name='projectenv'),
    url(r'^add/projectenv/$', views.add_projectenv, name='add_projectenv'),
    url(r'^del/projectenv/(\d+)/$', views.del_projectenv, name='del_projectenv'),
    url(r'^edit/projectenv/(\d+)/$', views.edit_projectenv, name='edit_projectenv'),

]
