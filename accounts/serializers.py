#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    
    phone_number = serializers.CharField(required=True)
    gender = serializers.CharField(required=False)
    date_of_birth = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        
        user.phone_number = self.validated_data.get('phone_number')
        user.genger = self.validated_data.get('gender')
        user.date_of_birth = self.validated_data.get('date_of_birth')
        user.state = self.validated_data.get('state')
        user.city = self.validated_data.get('city')
        user.save(update_fields=['phone_number', 'gender', 'date_of_birth', 'state', 'city'])