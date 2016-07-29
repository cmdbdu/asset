# coding:utf-8
from django.shortcuts import render
from django.template.response import TemplateResponse

from forms import CustomerForm, BomForm, DeviceForm
from models import Bom, Device

from utils.django_values_list_count import count_list
from django.contrib.auth.decorators import login_required

@login_required
def index(request, template):
    devices = Device.objects.all()

    import pdb
    if request.method == "POST":
        try:
            name = request.POST.getlist('bom_sns')
            if len(list(set(name))) == 1 and list(set(name))[0] == '':
                #全为空
                print "空"
                pass
            else:
                new_device = Device()
                for i in name:
                    try:
                        bom = Bom.objects.get(bom_sn=i)
                        print bom
                        if bom.bom_name == "ser":
                            new_device.device_sn = bom.bom_sn
                        new_device.save()
                        new_device.device_boms.add(bom)
                        #bom.bom_state = 'inuse'
                        #bom.save()
                        new_device.save()
                    except Exception,e:
                        print e
        except:
            pass

        cus_form = CustomerForm(request.POST)
        bom_form = BomForm(request.POST)

        if cus_form.is_valid():
            cus_form.save()
        if bom_form.is_valid():
            bom_form.save()
    else:
        cus_form = CustomerForm()
        bom_form = BomForm()
        device_form = DeviceForm()

    return TemplateResponse(request, template,{'cus_form':cus_form,
                                               'bom_form':bom_form,
                                               'devices':devices})


@login_required
def stock(request, template):
    boms_count = count_list(list(Bom.objects.values_list('bom_name','bom_status')))
    return TemplateResponse(request, template, {'boms_count':boms_count})
