#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('pages.urls')),
    path("accounts/", include('allauth.urls')),
    path('api/v1/', include('cab.urls')),
    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/registration/', include('rest_auth.registration.urls'))
]
