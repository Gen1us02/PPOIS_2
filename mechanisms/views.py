from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from .models import Mechanism
from .forms import AddMechanismForm


# Create your views here.
class MechanismsView(ListView):
    model = Mechanism
    template_name = "mechanisms/mechanisms.html"
    paginate_by = 4
    context_object_name = "mechanisms"

    def get_queryset(self):
        mechanisms = Mechanism.objects.all()
        return mechanisms


class MechanismCreateView(CreateView):
    model = Mechanism
    template_name = "mechanisms/add_mechanism.html"
    success_url = reverse_lazy("mechanisms:index")
    form_class = AddMechanismForm


class MechanismUpdateView(UpdateView):
    model = Mechanism
    template_name = "mechanisms/add_mechanism.html"
    success_url = reverse_lazy("mechanisms:index")
    form_class = AddMechanismForm

    def get_object(self, queryset=...):
        mechanism = Mechanism.objects.get(name=self.kwargs.get("mechanism_name"))
        return mechanism


class MechanismDeleteView(View):
    def post(self, request, *args, **kwargs):
        mechanism = Mechanism.objects.get(id=self.kwargs.get("mechanism_id"))
        mechanism.delete()

        return HttpResponseRedirect(reverse_lazy("mechanisms:index"))


class MechanismDetachView(View):
    def post(self, request, *args, **kwargs):
        mechanism = Mechanism.objects.get(id=self.kwargs.get("mechanism_id"))
        mechanism.robot_id = None
        mechanism.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))


class MechanismRepairView(View):
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("mechanism_id")
        if id:
            mechanism = Mechanism.objects.get(id=id)
            mechanism.damage = 0
            mechanism.save()
        else:
            Mechanism.objects.all().update(damage=0)

        return HttpResponseRedirect(reverse_lazy("mechanisms:index"))
