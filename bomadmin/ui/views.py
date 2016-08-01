# coding:utf-8
from django.shortcuts import render
from django.template.response import TemplateResponse

from forms import CustomerForm, BomForm, DeviceForm
from models import Bom, Device, Customer

from utils.django_values_list_count import count_list
from django.contrib.auth.decorators import login_required

@login_required
def index(request, template):
    devices = Device.objects.all()

    if request.method == "POST":
        try:
            name = request.POST.getlist('bom_sns')
            if len(list(set(name))) == 1 and list(set(name))[0] == '':
                #全为空
                pass
            else:
                new_device = Device()
                dev = {}
                for i in name:
                    try:
                        bom = Bom.objects.get(bom_sn=i)
                        if bom.bom_name == u'ser' and dev.has_key(u'ser'):
                            print 'too many server'
                        else:
                            dev[bom.bom_name] = (bom, bom.bom_sn)

                    except Exception,e:
                        print e
                if dev.has_key('ser'):
                    new_device.device_sn = dev['ser'][1]
                    bom = Bom.objects.get(bom_sn=dev['ser'][1])
                    bom.bom_status = 'inuse'
                    bom.save()
                    new_device.save()
                    for key in dev:
                        if key != 'ser':
                            new_device.device_boms.add(dev[key][0])
                            dev[key][0].bom_status = 'inuse'
                            dev[key][0].save()

                    new_device.save()
        except:
            pass

        cus_form = CustomerForm(request.POST)
        bom_form = BomForm(request.POST)
        if cus_form.is_valid():
            cus_form.save()
        else:
            err_msg = u"添加失败"
        if bom_form.is_valid():
            bom_form.save()
        else:
            print bom_form.non_field_errors()
            print bom_form.errors
            err_msg = u"添加失败"
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

@login_required
def device(request, device_id, template):
    device = Device.objects.get(id=device_id)
    print dir(device)
    print device.device_user
    users = Customer.objects.all()
    if request.method == "GET":
        return TemplateResponse(request, template, {'device':device,
                                                    'users':users})
    else:
        cus_id = request.POST.get('cus_id')
        device.device_user = Customer.objects.get(id=cus_id)
        device.device_status = 'inuse'
        device.save()
        return TemplateResponse(request, template, {'device':device,
                                                    'users':users})

