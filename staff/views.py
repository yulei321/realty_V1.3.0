# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def emp_list(request):
    return render(request, 'emp_list.html')


def house_list(request):
    return render(request, 'house_list.html')


def house_type_list(request):
    return render(request, 'house_type_list.html')


def dept_list(request):
    return render(request, 'dept_list.html')


def notice_list(request):
    return render(request, 'notice_list.html')