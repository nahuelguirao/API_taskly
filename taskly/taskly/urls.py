from django.contrib import admin
from django.urls import path, include
from users.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', include('tasks.api.routers')),
    path('', include('users.api.routers'))
]
