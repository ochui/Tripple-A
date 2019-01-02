#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class CustomUser(AbstractUser):

    GENDER = (
        ('M', _('MALE')),
        ('F', _('FEMALE'))
    )

    avatar = models.ImageField(_("avatar"), upload_to='avatars/%Y/%m/%d/', blank=True)
    gender = models.CharField(_("gender"), max_length=50, choices=GENDER)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    phone_number = models.CharField(_("phone number"), max_length=20, null=True, blank=True)
    state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()