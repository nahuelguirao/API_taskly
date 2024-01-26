from rest_framework import generics, status
from rest_framework.response import Response
from tasks.models import Task
from tasks.api.serializer import TaskSerializer


class TaskListCreateAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.all()

    def post(self, request):
        new_task = self.serializer_class(data=request.data)
        
        if new_task.is_valid():
            new_task.save()
            return Response({'message':'Task saved.'}, status.HTTP_201_CREATED)
        
    
    