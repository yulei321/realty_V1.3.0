# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
# 客户信息
def customer_list1(request):

    cust_list = CustomerInfo.objects.all()

    return render(request, 'customer_list1.html', {'cust_list': cust_list})


 # 客户信息编辑
def customer_edit(request):
    cust_list_bj = CustomerInfo.objects.create()
    return render(request, 'customer_edit.html', {'cust_list_bj': cust_list_bj})

# 客户详情
def customer_detail(request):
    return render(request, 'customer_detail.html')

# 添加客户信息
def customer_add(request):

    return render(request,'customer_add.html')


# 客户分配信息目录
def customer_distribute_list(request):
    cust_dist_list = CustomerLinkreord.objects.all()
    return render(request, 'customer_distribute_list.html',{'cust_dist_list':cust_dist_list})

# 分配所选客户信息
def customer_distribute(request):
    return render(request, 'customer_distribute.html')


# 客户关怀信息目录
def customer_care_list(request):
    cust_care_list = CustomerCare.objects.all()
    return render(request, 'customer_care_list.html', {'cust_care_list':cust_care_list})


def customer_care_edit(request):
    return render(request, 'customer_edit.html')
# 客户类型信息目录
def customer_type_list(request):
    cust_type_list = CustomerType.objects.all()
    return render(request, 'customer_type_list.html',{'cust_type_list':cust_type_list})

# 客户状态信息目录
def customer_state_list(request):
    cust_stat_list = CustomerStatus.objects.all()
    return render(request, 'customer_state_list.html',{'cust_stat_list': cust_stat_list})

# 客户来源信息目录
def customer_source_list(request):
    cust_source_list = CustomerSource.objects.all()
    cust_source_list_del = CustomerSource .objects.filter()
    return render(request, 'customer_source_list.html', {'cust_source_list':cust_source_list},{'cust_source_list_del':cust_source_list_del})

    print(cust_source_list)


