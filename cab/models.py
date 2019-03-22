#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
import uuid
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Driver(models.Model):
    
    DRIVER_STATUS = (
        ('1', 'Approved'),
        ('0', 'Awaiting Approval')
    )

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.CharField(max_length=50)
    plate_no = models.CharField(max_length=15)
    status = models.CharField(max_length=50, choices=DRIVER_STATUS, default='0')
    location = models.PointField(null=True, blank=True)
    socket_id = models.UUIDField(default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.driver.get_full_name()


class Company(models.Model):

    COMPANY_STATUS = (
        ('1', 'Approved'),
        ('2', 'Suspended'),
        ('0', 'Awaiting Approval')
    )

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=COMPANY_STATUS, default='0')
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Route(models.Model):

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pick_up = models.CharField('From', max_length=50)
    drop_off = models.CharField('To', max_length=50)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    two_way = models.BooleanField(default=True)
    

    def __str__(self):
        if self.two_way:
            return '{0}:{1} to {2}(Return)'.format(self.company.name, self.pick_up, self.drop_off)
        else:
            return '{0}:{1} to {2}'.format(self.company.name, self.pick_up, self.drop_off)


class Booking(models.Model):

    BOOKING_STATUS = (
        ('1', 'SEARCHING FOR DRIVER'),
        ('2', 'WAITING FOR PICKUP'),
        ('3', 'IN PROGRESS'),
        ('4', 'COMPLETED'),
        ('5', 'CANCEL')
    )

    BILLING_STATUS = (
        ('0', 'UNPAID'),
        ('1', 'PAID')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = JSONField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True)
    billing_status = models.CharField("Billing status", max_length=2, choices=BILLING_STATUS, default='0')
    payment_time = models.DateTimeField("Payment time", auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=2, choices=BOOKING_STATUS, default='1')
    booking_time = models.DateTimeField("Booking time", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def name_with_phone_number(self):
        return '{0}({1})'.format(self.user.get_full_name(), self.user.phone_number)

    def __str__(self):
        return '{0}({1})'.format(self.user.get_full_name(), self.user.phone_number)


class Car(models.Model):
    
    DRIVER_STATUS = (
        ('1', 'Available'),
        ('0', 'Unavailable')
    )

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    model = models.CharField(max_length=50)
    plate_no = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField() #LOL, not anti-christ
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to = 'cars/', default = 'cars/no-img.jpg')
    status = models.CharField(max_length=50, choices=DRIVER_STATUS, default='0')


    def __str__(self):
        return self.model