#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    
    phone_number = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        
        user.phone_number = self.validated_data.get('phone_number')
        user.save(update_fields=['phone_number'])