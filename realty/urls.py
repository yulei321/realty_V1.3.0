# coding=utf-8
"""realty URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录界面模块
    url(r'^login/', include('home.urls')),
    # 主界面功能模块
    url(r'^main/', include('home.urls')),
    # 客户功能模块
    url(r'^client/', include('client.urls')),
    # 员工功能模块
    url(r'^staff/', include('staff.urls')),
    # 管理员模块
    url(r'^adminlist/', include('adminlist.urls')),



]
