# coding=utf-8

from django.conf.urls import url

from client import views

urlpatterns = [
    # 客户信息
    url(r'^customer_list1.html', views.customer_list1),
    # 客户信息编辑
    url(r'^customer_edit.html', views.customer_edit),
    # 客户详情
    url(r'^customer_detail.html', views.customer_detail),
    # 添加客户信息
    url(r'^customer_add.html', views.customer_add),
    # 客户分配信息目录
    url(r'^customer_distribute_list.html', views.customer_distribute_list),
    # 分配所选客户信息
    url(r'^customer_distribute.html', views.customer_distribute),
    # 客户关怀信息目录
    url(r'^customer_care_list.html', views.customer_care_list),
    url(r'^customer_care_edit.html', views.customer_care_edit),

    # 客户来源查询
    url(r'^customer_type_list.html', views.customer_type_list),
    # 客户状态信息目录
    url(r'^customer_state_list.html', views.customer_state_list),
    # 客户来源信息目录
    url(r'^customer_source_list.html', views.customer_source_list),
    # 客户来源添加
    url(r'^customer_source_add.html', views.customer_source_add),
    # 客户来源删除
    url(r'^customer_source_list_dele', views.customer_source_list_dele),
    # 分页展示
    url(r'^customer_source_list_tab', views.customer_source_list_tab),
    # 客户类型添加
    url(r'^customer_type_add.html', views.customer_type_add),
    # 客户类型删除
    url(r'^customer_type_dele.html', views.customer_type_dele),
    # 客户状态删除
    url(r'^customer_state_dele.html', views.customer_state_dele),
    # 客户状态添加
    url(r'^customer_state_add.html', views.customer_state_add),
]