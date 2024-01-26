from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.api.serializer import UserSignInSerializer

class UsersSignInViewSet(ViewSet):
    serializer_class = UserSignInSerializer
    
    def create(self, request):
        new_user = self.serializer_class(data = request.data)
        
        if new_user.is_valid():
            new_user.save()
            
            token = Token.objects.create(user=new_user.instance)
            
            return Response({'user': {
                'id': new_user.data['id'],
                'username': new_user.data['username'],
                'token': token.key
                }}, status.HTTP_201_CREATED)
        
        return Response({'error':new_user.errors}, status.HTTP_400_BAD_REQUEST)