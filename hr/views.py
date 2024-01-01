from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,UpdateView,DetailView
from hr.forms import Loginform,CategoryForm,JobForm,JobChangeForm
from django.contrib.auth import authenticate,login,logout
from myapp.models import Category,Jobs,Applications
from django.urls import reverse_lazy
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class SigninView(FormView):
    template_name="signin.html"
    form_class=Loginform
   
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print("success")
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("seeker_index")
        print("error")
        return render(request,"signin.html",{"form":form})
    
    
class DashboardView(TemplateView):
    template_name="index.html"  

class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

# class CategoryView(View):
#    def get(self,request,*args,**kwargs):
#         form=CategoryForm()
#         qs=Category.objects.all()
#         return render(request,"category.html",{"form":form, "data":qs})
   
#    def post(self,request,*args,**kwargs):
#        form=CategoryForm(request.POST)
#        if form.is_valid():
#            form.save()
#            print("category added")
#            return redirect("category")
#        else:
#            print("error")
#            return redirect("category")
class catogarylistView(CreateView,ListView):
    template_name="category.html"
    form_class=CategoryForm
    success_url=reverse_lazy("category")#url name category
    context_object_name="data"
    model=Category
    def form_valid(self, form):
        messages.success(self.request,"added")
        return super().form_valid(form)


class CategoryDeleteView(View):
   def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        print(id)
        Category.objects.get(id=id).delete()
        return redirect('category')
   
class JobCreatView(CreateView):
    template_name="job_add.html"
    form_class=JobForm
    success_url=reverse_lazy('job-all')

class JobListView(ListView):
    template_name="job_list.html"
    context_object_name="jobs"
    model=Jobs
    # def get(self,request,*args,**kwargs):
    #     qs=Jobs.objects.all()
    #     if "status" in request.GET:
    #         value=request.GET.get("status")
    #         qs=qs.filter(status=value)
    #         return render(request,self.template_name,{"jobs":qs})



    # def get_queryset(self) :
    #     return Jobs.objects.filter(status=True)#status true allel list n ozhivaakki list cheyyan
                                                #orm query change
class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Jobs.objects.get(id=id).delete()
        return redirect("job-all")
    
class JobUpdateView(UpdateView):
    form_class=JobChangeForm
    template_name="job_edit.html"
    model=Jobs
    success_url=reverse_lazy("job-all")

class JobApplicationlistView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_obj=Jobs.objects.get(id=id)
        qs=Applications.objects.filter(job=job_obj)
        return render(request,"applications.html",{"data":qs})

class ApplicationDetailView(DetailView):
    template_name="application_detail.html"
    context_object_name="application"
    model=Applications
    
class ApplicationUpdateView(View):
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        applications_object=Applications.objects.get(id=id)
        applicant_mails=applications_object.student.email
        value=request.POST.get("status")
        Applications.objects.filter(id=id).update(status=value)
       

        if value=="shortlisted":
                        send_mail(
                "Your application status has been change",
                "You application has been changed 2nd",
                "kamohamedshahil@gmail.com",
                ["shahilshx007@gmail.com"],
                fail_silently=False,
            )

        return redirect("index")