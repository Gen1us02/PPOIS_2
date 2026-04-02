from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, View
from software.forms import AddSoftwareForm
from .models import Robot, Phrases, RobotStatus
from .forms import AddRobotForm, AddPhraseForm


# Create your views here.
class RobotView(DetailView):
    template_name = "robot/robot.html"

    def get_object(self, queryset=...):
        robot = Robot.objects.all().first()
        return robot
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        robot = self.get_object()
        phrases = Phrases.objects.filter(robot_id=robot)
        context["robot"] = robot
        context["phrases"] = phrases
        context["form"] = AddSoftwareForm()
        return context


class RobotCreateView(CreateView):
    model = Robot
    template_name = "robot/add_robot.html"
    success_url = reverse_lazy("robot:index")
    form_class = AddRobotForm


class RobotDeleteView(View):
    def post(self, request, *args, **kwargs):
        robot = Robot.objects.get(name=self.kwargs.get("robot_name"))
        robot.delete()

        return HttpResponseRedirect(reverse_lazy("robot:index"))


class RobotEditView(UpdateView):
    model = Robot
    template_name = "robot/add_robot.html"
    success_url = reverse_lazy("robot:index")
    form_class = AddRobotForm

    def get_object(self, queryset=...):
        robot = Robot.objects.get(name=self.kwargs.get("robot_name"))
        return robot

    def get_initial(self):
        initial = super().get_initial()
        robot = self.get_object()
        initial.update({"name": robot.name, "speed": robot.speed, "image": robot.image})
        return initial


class PhraseCreateView(CreateView):
    model = Phrases
    template_name = "robot/learn_phrase.html"
    success_url = reverse_lazy("robot:index")
    form_class = AddPhraseForm

    def form_valid(self, form):
        robot = Robot.objects.get(name=self.kwargs.get("robot_name"))
        phrase = form.save(commit=False)
        phrase.robot_id = robot
        phrase.save()
        return HttpResponseRedirect(self.success_url)
    

class RobotSoftwareDetachView(View):
    def post(self, request, *args, **kwargs):
        robot = Robot.objects.get(name=self.kwargs.get("robot_name"))
        robot.software = None
        robot.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))
    
    
class RobotChargeView(View):
    def post(self, request, *args, **kwargs):
        robot = Robot.objects.get(id=self.kwargs.get("robot_id"))
        robot.battery = 100
        robot.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))
    
    
class RobotEnableView(View):
    def post(self, request, *args, **kwargs):
        robot = Robot.objects.get(id=self.kwargs.get("robot_id"))
        curr_status = robot.status
        if curr_status.name != "Разряжен":
            robot.status = RobotStatus.objects.get(name=("Неактивен" if robot.status.name == "Активен" else "Активен"))
        else:
            pass
        robot.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))
    
    
class RobotRepairView(View):
    def post(self, request, *args, **kwargs):
        robot = Robot.objects.get(id=self.kwargs.get("robot_id"))
        robot.mechanisms.all().update(damage=0)
        robot.sensors.all().update(damage=0)
        robot.save()

        return HttpResponseRedirect(reverse_lazy("robot:index"))
    
