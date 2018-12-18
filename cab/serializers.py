#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from cab.models import Driver, Company, Route


class DriverSerializer(ModelSerializer):
    driver = ReadOnlyField(source='driver.get_full_name')

    class Meta:
        model = Driver
        fields = (
            'id', 'driver', 'car', 
            'plate_no', 'status'
        )

        read_only_fields = (
            'status',
        )


class CompanySerializer(ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = (
            'status',
        )


class RouteSerializer(ModelSerializer):
    
    class Meta:
        model = Route
        fields = '__all__'
