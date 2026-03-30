from software.models import Software


class ContextSoftwareMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_software = Software.objects.all()
        context["all_software"] = all_software
        return context
