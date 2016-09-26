#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request, template):
    return TemplateResponse(request, template)
