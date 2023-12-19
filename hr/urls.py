from django.urls import path
from hr import views

urlpatterns = [
    path("",views.SigninView.as_view(),name="signin"),
    path("index",views.DashboardView.as_view(),name="index"),
    path("signout",views.SignoutView.as_view(),name="signout"),
    path("category",views.catogarylistView.as_view(),name="category"),
    path("remove/<int:pk>",views.CategoryDeleteView.as_view(),name="delete"),
    path("job/add",views.JobCreatView.as_view(),name="job-add"),
    path("job/all",views.JobListView.as_view(),name="job-all"),
    path("job/<int:pk>/remove",views.JobDeleteView.as_view(),name="job-delete"),
    path("job/<int:pk>/change",views.JobUpdateView.as_view(),name="job-edit")

]
