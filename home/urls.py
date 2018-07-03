#coding=utf-8

from django.conf.urls import url

from home import views

urlpatterns = {
    url(r'^$', views.login),
    # 主界面
    url(r'^main.html', views.main),
    # 上部模块
    url(r'^top.html', views.top),
    # 左部模块
    url(r'^left.html', views.left),
    # 右部模块
    url(r'^center.html', views.center),
    # 下部模块
    url(r'^down.html', views.down),

}