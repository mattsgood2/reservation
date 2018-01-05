from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    time = models.DateTimeField()

    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reservation {0} - {1}'.format(self.pk, self.name)
        
