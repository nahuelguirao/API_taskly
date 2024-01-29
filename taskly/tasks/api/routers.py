from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.api.views import TaskViewSet


router = DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    *router.urls,
    path('get_tasks/user/<int:pk>/', TaskViewSet.as_view({'get':'user_task'})),
    path('update_task/<str:uuid>/', TaskViewSet.as_view({'put':'update_task'})),
    path('delete_task/<str:uuid>/', TaskViewSet.as_view({'delete':'delete_task'}))
]