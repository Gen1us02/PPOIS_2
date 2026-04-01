from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from .models import Software
from .forms import AddSoftwareForm


# Create your views here.
class SoftwareView(ListView):
    model = Software
    template_name = "software/software.html"
    context_object_name = "all_software"
    paginate_by = 4

    def get_queryset(self):
        all_software = Software.objects.all()
        return all_software


class SoftwareCreateView(CreateView):
    model = Software
    template_name = "software/add_software.html"
    success_url = reverse_lazy("software:index")
    form_class = AddSoftwareForm


class SoftwareEditView(UpdateView):
    model = Software
    template_name = "software/add_software.html"
    success_url = reverse_lazy("software:index")
    form_class = AddSoftwareForm

    def get_object(self, queryset=...):
        software = Software.objects.get(id=self.kwargs.get("software_id"))
        return software

    def get_initial(self):
        initial = super().get_initial()
        software = self.get_object()
        initial.update(
            {
                "software_type": software.software_type,
                "version": software.version,
                "size": software.size,
                "creator": software.creator,
            }
        )
        return initial


class SoftwareDeleteView(View):
    def post(self, request, *args, **kwargs):
        software = Software.objects.get(id=self.kwargs.get("software_id"))
        software.delete()

        return HttpResponseRedirect(reverse_lazy("software:index"))
