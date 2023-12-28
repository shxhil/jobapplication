from django.urls import path

from jobseeker import views
urlpatterns = [
           path("register/",views.SignUpView.as_view(),name="signup"),
           path("index/",views.StudentIndexView.as_view(),name="seeker_index"),
           path("profiles/add",views.ProfileCreateView.as_view(),name="profile_add"),
           path("profiles/<int:pk>/",views.ProfileDetailView.as_view(),name="profile_detail"),
           path("profile/<int:pk>/change",views.ProfileEditView.as_view(),name="profile_edit"),
           path("jobs/<int:pk>",views.JobDetailView.as_view(),name="job-detail"),
           path("jobs/<int:pk>/apply",views.ApplyJobView.as_view(),name="job_apply"),
           path("applications/all",views.ApplicationListView.as_view(),name="myapplications"),
           path("jobs/<int:pk>/save",views.JobSaveView.as_view(),name="job_save"),
           path("jobs/<int:pk>/all",views.SavedJobsListView.as_view(),name="saved_jobs"),


]