#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cab.models import Route, Driver, Company
from cab.serializers import RouteSerializer, CompanySerializer, DriverSerializer


class RouteList(ListCreateAPIView):

    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        
        return Route.objects.all()



class CompanyList(ListCreateAPIView):
    
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Company.objects.all()

class DriverList(ListCreateAPIView):
    
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Driver.objects.all()

    def perform_create(self, serializer):
        serializer.save(driver=self.request.user)