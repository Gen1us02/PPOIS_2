from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from .models import Sensor
from .forms import AddSensorForm


# Create your views here.
class SensorsView(ListView):
    model = Sensor
    template_name = "sensors/sensors.html"
    paginate_by = 4
    context_object_name = "sensors"

    def get_queryset(self):
        sensors = Sensor.objects.all()
        return sensors


class SensorCreateView(CreateView):
    model = Sensor
    template_name = "sensors/add_sensor.html"
    success_url = reverse_lazy("sensors:index")
    form_class = AddSensorForm
    
    def form_valid(self, form):
        sensor = form.save(commit=False)
        if self.request.POST.get("robot_id", None):
            sensor.is_active = True
        else:
            sensor.is_active = False
        sensor.save()
        return super().form_valid(form)
    


class SensorEditView(UpdateView):
    model = Sensor
    template_name = "sensors/add_sensor.html"
    success_url = reverse_lazy("sensors:index")
    form_class = AddSensorForm

    def get_object(self, queryset=...):
        sensor = Sensor.objects.get(id=self.kwargs.get("sensor_id"))
        return sensor
    
    def form_valid(self, form):
        sensor = form.save(commit=False)
        if self.request.POST.get("robot_id", None):
            sensor.is_active = True
        else:
            sensor.is_active = False
        sensor.save()
        return super().form_valid(form)


class SensorDeleteView(View):
    def post(self, request, *args, **kwargs):
        sensor = Sensor.objects.get(id=self.kwargs.get("sensor_id"))
        sensor.delete()

        return HttpResponseRedirect(reverse_lazy("sensors:index"))
    
    
class SensorDetachView(View):
    def post(self, request, *args, **kwargs):
        sensor = Sensor.objects.get(id=self.kwargs.get("sensor_id"))
        sensor.robot_id = None
        sensor.is_active = False
        sensor.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))
    
    
class SensorRepairView(View):
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("sensor_id")
        if id:
            sensor = Sensor.objects.get(id=id)
            sensor.damage = 0
            sensor.save()
        else:
            Sensor.objects.all().update(damage=0)

        return HttpResponseRedirect(reverse_lazy("sensors:index"))
