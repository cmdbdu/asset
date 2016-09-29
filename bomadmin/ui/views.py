# coding:utf-8
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect

from forms import CustomerForm, BomForm, DeviceForm
from models import Bom, Device, Customer

from assets.models import Assets
from assets.forms import AssetsFrom

from utils.django_values_list_to_json import count_list
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def get_handler_404_or_500(request):
    return HttpResponseRedirect(reverse('index'))

@login_required
def index(request, template):
    user = request.user
    devices = Device.objects.all()
    assets = Assets.objects.all()
    pag_list = []

    import pdb
    if user.get_profile().asset_edit:
        pag_list += assets
        if user.get_profile().parts_edit:
            pag_list += devices

    elif user.get_profile().parts_edit:
        pag_list += devices

    cus_form = CustomerForm()
    bom_form = BomForm()
    device_form = DeviceForm()
    asset_form = AssetsFrom()

    if request.method == "POST":
        if request.POST['subname'] == 'add_device':
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
                                pass
                            else:
                                dev[bom.bom_name] = (bom, bom.bom_sn)

                        except Exception,e:
                            pass
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
                        return HttpResponseRedirect(reverse('index'))
            except:
                pass
        elif request.POST['subname'] == 'add_cus':
            cus_form = CustomerForm(request.POST)
            if cus_form.is_valid():
                cus_form.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                err_msg = 'error'
        elif request.POST['subname'] == 'add_asset':
            asset_form = AssetsFrom(request.POST)
            if asset_form.is_valid():
                asset_form.save()
                return HttpResponseRedirect(reverse('index'))
        else:
            bom_form = BomForm(request.POST)
            if bom_form.is_valid():
                bom_form.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                err_msg = 'error'

    page = request.GET.get('page', '')
    paginator = Paginator(pag_list,'10')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page('1')
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return TemplateResponse(request, template,{'cus_form':cus_form,
                                               'bom_form':bom_form,
                                               'devices':devices,
                                               'asset_form':asset_form,
                                               'contacts':contacts,
                                               'pages':paginator})


@login_required
def stock(request, template):
    boms_count = count_list(list(Bom.objects.values_list('bom_name',
                                                        'bom_status',
                                                        'bom_sn')
                                )
                            )
    cus_form = CustomerForm()
    bom_form = BomForm()
    return TemplateResponse(request, template, {'boms_count':boms_count,
                                                'bom_form':bom_form,
                                                'cus_form':cus_form})

@login_required
def device(request, device_id, template):
    device = Device.objects.get(id=device_id)
    users = Customer.objects.all()
    if request.method == "GET":
        return TemplateResponse(request, template, {'device':device,
                                                    'users':users})
    else:
        cus_id = request.POST.get('cus_id')
        try:
            device.device_user = Customer.objects.get(id=cus_id)
            device.device_status = 'inuse'
            device.save()
        except Exception,e:
            pass
        return TemplateResponse(request, template, {'device':device,
                                                    'users':users})

@login_required
def asset(request, asset_id, template):
    asset = Assets.objects.get(id=asset_id)
    users = Customer.objects.all()
    if request.method == 'GET':
        return TemplateResponse(request, template, {'asset':asset,
                                                    'users':users}
                                )

@login_required
@csrf_exempt
def edit(request):
    value = request.POST['value']
    asset_id = request.POST['asset_id']
    asset = Assets.objects.get(id=asset_id)
    asset.asset_to = value
    if value:
        asset.asset_status='inuse'
    else:
        asset.asset_status='store'
    asset.save()
    return HttpResponse({'status':'OK'})
