from reservation.settings import celery_app
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from timezone_field import TimeZoneField

import arrow

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='GB')


    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reservation {0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('views.reservation', args=[str(self.id)])

    def clean(self):
        reservation_time = arrow.get(self.time)
