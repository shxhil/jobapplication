from django.urls import path

from jobseeker import views
urlpatterns = [
           path("register/",views.SignUpView.as_view(),name="signup"),
           path("index/",views.StudentIndexView.as_view(),name="seeker_index"),
           path("profiles/add",views.ProfileCreateView.as_view(),name="profile_add"),
           path("profiles/<int:pk>/",views.ProfileDetailView.as_view(),name="profile_detail"),
           path("profile/<int:pk>/change",views.ProfileEditView.as_view(),name="profile_edit"),
           path("jobs/<int:pk>",views.JobDetailView.as_view(),name="job-detail")


]