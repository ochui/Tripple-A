#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class PhoneNumberBackend:
    def __init__(self, *args, **kwargs):
        self.user_model = get_user_model()
    """
    authenticate user using phone number
    """

    def authenticate(self, request, username=None, password=None):
        if username is None:
            return None

        try:
            user = self.user_model.objects.get(phone_number=username)
        except self.user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            user = self.user_model._default_manager.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None


class EmailBackend:
    def __init__(self, *args, **kwargs):
        self.user_model = get_user_model()
    """
    authenticate user using email
    """

    def authenticate(self, request, username=None, password=None):
        if username is None:
            return None

        try:
            user = self.user_model.objects.get(email=username)
        except self.user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            user = self.user_model._default_manager.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
