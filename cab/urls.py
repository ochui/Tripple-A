#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.urls import path
from cab.views import RouteList, CompanyList, DriverList
urlpatterns = [
    path('routes', RouteList.as_view(), name='routes'),
    path("companies", CompanyList.as_view(), name="companies"),
    path("drivers", DriverList.as_view(), name="drivers")
]