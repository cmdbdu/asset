# coding:utf8
from django.contrib import admin
from models import (Customer, CustomerAdmin,
                    Bom, BomAdmin,
                    Device, DeviceAdmin)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bom, BomAdmin)
admin.site.register(Device, DeviceAdmin)
