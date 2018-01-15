from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Reservation

# Create your views here.
class ReservationListView(ListView):
    model = Reservation

class ReservationDetailView(DeleteView):
    model = Reservation

class ReservationCreateView(SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'time']
    success_message = 'Reservation Successfully Booked.'

class ReservationUpdateView(SuccessMessageMixin, UpdateView):
    model = Reservation
    fields = ['name', 'mobile_number', 'time']
    success_message = 'Reservation Successfully Updated'

class ReservationDetailView(SuccessMessageMixin, DeleteView):
    model = Reservation
    success_url = reverse_lazy(list_reservations)
