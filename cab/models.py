#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.db import models
from django.conf import settings


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