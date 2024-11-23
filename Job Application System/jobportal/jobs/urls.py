from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('admin/add-job/', views.add_job, name='add_job'),
    path('admin/applications/<int:job_id>/', views.view_applications, name='view_applications'),
]
