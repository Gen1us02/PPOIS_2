from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, View
from .models import Robot, Phrases
from .forms import AddRobotForm, AddPhraseForm


# Create your views here.
class RobotView(DetailView):
    template_name = "robot/robot.html"

    def get_object(self, queryset=...):
        robot = Robot.objects.all()
        return robot[0] if robot else None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        robot = self.get_object()
        phrases = Phrases.objects.filter(robot_id=robot)
        context["robot"] = robot
        context["phrases"] = phrases
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
