#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib import admin
from cab.models import Company, Route, Driver

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'admin')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    
    list_display = ('company', 'pick_up', 'drop_off', 'cost')
    list_filter = ('company', 'pick_up', 'drop_off')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    
    list_display = ('driver', 'car', 'plate_no', 'status')
    list_filter = ('status', )

