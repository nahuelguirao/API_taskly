from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from tasks.models import Task
from tasks.api.serializer import TaskSerializer

        
class TaskViewSet(ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def create(self, request):
        new_task_serializer = TaskSerializer(data = request.data)
        
        if new_task_serializer.is_valid():
            new_task_serializer.save()
            return Response({'message':'Task saved correctly.'}, status.HTTP_201_CREATED)
        
        return Response({'error':new_task_serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True,methods=['get'])
    def user_task(self, request, pk = None):
        tasks = Task.objects.filter(user=pk)
        all_tasks = TaskSerializer(tasks, many = True)
        return Response(all_tasks.data, status.HTTP_200_OK)
    
    @action(detail=False, methods=['update'])
    def update_task(self,request, uuid = None):
        old_task = Task.objects.filter(uuid = uuid).first()
        
        if not old_task:
            return Response({'error':'Task not found.'}, status.HTTP_404_NOT_FOUND)
        
        edited_task_serializer = TaskSerializer(old_task, data = request.data, partial = True)
        
        if edited_task_serializer.is_valid():
            edited_task_serializer.save()
            return Response({'message':'Task updated correctly.'}, status.HTTP_200_OK)

        return Response({'message':edited_task_serializer.errors}, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['destroy'])
    def delete_task(self, request, uuid = None):
        task_to_delete = Task.objects.filter(uuid=uuid).first()
        
        if task_to_delete:
            task_to_delete.delete()
            return Response({'message':'Task deleted.'}, status.HTTP_200_OK)
        
        return Response({'error':'Task not found'}, status.HTTP_404_NOT_FOUND)
        
    
    