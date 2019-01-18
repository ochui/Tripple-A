#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from cab.models import Route, Driver, Company, Booking
from cab.serializers import RouteSerializer, CompanySerializer, DriverSerializer, BookingSerializer, BookingDetailSerializer


class RouteList(ListCreateAPIView):

    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        
        return Route.objects.filter(company=self.kwargs['company_id'])



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


class BookingList(ListCreateAPIView):

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingDetails(RetrieveUpdateDestroyAPIView):
    
    serializer_class = BookingDetailSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)