#coding:utf-8


from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_views(request):
    logout(request)
    return redirect('/accounts/login')


