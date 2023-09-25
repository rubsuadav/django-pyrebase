from django.urls import path
from .views import JobView

urlpatterns = [
    path('jobs', JobView.as_view()),
    path('jobs/<str:job_id>', JobView.as_view()),
]
