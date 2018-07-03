# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 登录界面
def login(request):

    return render(request, 'login.html')

# 主界面
def main(request):
    return render(request, 'main.html')

def top(request):
    return render(request, 'top.html')


def left(request):
    return render(request, 'left.html')


def center(request):
    return render(request, 'center.html')


def down(request):
    return render(request, 'down.html')