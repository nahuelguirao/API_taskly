from django.urls import path
from tasks.api.api import TaskListCreateAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='tasks list')
]