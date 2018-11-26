#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.urls import path
from accounts.api_views import CustomRegistrationView

urlpatterns = [
    path('register', CustomRegistrationView.as_view(), name='register'),
]
