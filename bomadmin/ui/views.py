# coding:utf-8
from django.shortcuts import render

print 'ui.views'
def index(request, template):
    return render(request, template)

