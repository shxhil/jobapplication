from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
# Create your views here.
from myapp.models import StudentProfile,Jobs
from django.urls import reverse_lazy
from jobseeker.forms import RegistrationForm,ProfileForm


class SignUpView(CreateView):
    template_name="jobseeker/register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")

class StudentIndexView(ListView):
    template_name="jobseeker/index.html"
    model=Jobs
    context_object_name="jobs"
    def get_queryset(self):
        qs=Jobs.objects.all().order_by("-created_date")#- is for descenting order
        return qs

class ProfileCreateView(CreateView):
    template_name="jobseeker/profile_add.html"
    form_class=ProfileForm
    success_url=reverse_lazy("seeker_index")
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class ProfileDetailView(DetailView):
    template_name="jobseeker/profile_detail.html"
    context_object_name="data"
    model=StudentProfile
   
class ProfileEditView(UpdateView):
    template_name="jobseeker/profile_edit.html"
    form_class=ProfileForm
    model=StudentProfile
    success_url=reverse_lazy("seeker_index")

class JoblistView(ListView):
    template_name="jobseeker/job_list.html"
    context_object_name="jobs"
    model=Jobs

class JobDetailView(DetailView):

    template_name="jobseeker/job_detail.html"
    model=Jobs
    context_object_name="data"