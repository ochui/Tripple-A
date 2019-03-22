#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.urls import path
from cab.views import RouteList, CompanyList, DriverList, BookingList, BookingDetails, NearbyDrivers, CarList
urlpatterns = [
    path('routes/<int:company_id>', RouteList.as_view(), name='routes'),
    path("companies", CompanyList.as_view(), name="companies"),
    path("drivers", DriverList.as_view(), name="drivers"),
    path("drivers/<longitude>/<latitude>", NearbyDrivers.as_view(), name="drivers_near_me"),
    path("booking", BookingList.as_view(), name="booking"),
    path("booking/<int:pk>", BookingDetails.as_view(), name="booking_details"),
    path("cars", CarList.as_view(), name="cars")
]
