#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'city', 'state')}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'city', 'state')}),
    )
    list_display = ['username', 'email', 'phone_number',  'city', 'state']
    list_filter = ['city', 'state', 'is_active', 'is_staff']
    model = CustomUser
