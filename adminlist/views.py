# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import DepartmentInfo


def emp_add(request):

    return render(request, 'emp_list.html')


def dept_add(request):
    if request.method == 'GET':
        return render(request, 'dept_add.html')
    else:
        dep_name = request.POST.get('departmentName', None)
        dep_desc = request.POST.get('departmentDesc', None)
        depart1 = 'NOT'
        try:
            depart1 = DepartmentInfo.objects.get(department_name=dep_name, department_desc=dep_desc)
        except DepartmentInfo.DoesNotExist:
            depart2 = DepartmentInfo.objects.create(department_name=dep_name, department_desc=dep_desc)
        if depart1 != 'NOT':
            return HttpResponse('记录已存在')
        elif depart2:
            return HttpResponse('添加成功')
        else:
            return HttpResponse('添加失败')



