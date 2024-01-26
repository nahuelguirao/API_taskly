from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.api.serializer import UserLoginSerializer

class Login(ObtainAuthToken):
    
    def post(self, request):
        #Serializes the request.data
        login_serializer = self.serializer_class(data=request.data)

        #If it's valid creates a token
        if login_serializer.is_valid():
            #Gets user
            user = login_serializer.validated_data['user']
            
            token, created = Token.objects.get_or_create(user = user)
            user_serializer = UserLoginSerializer(user)
            
            return Response({
                    'user':{
                        'id': user_serializer.data['id'],
                        'username': user_serializer.data['username'],
                        'token': token.key
                    }    
                }, status.HTTP_200_OK) 
                
                
        return Response({'error':'Invalid credentials.'}, status.HTTP_400_BAD_REQUEST)
    
class Logout(APIView):
    def post(self, request):
        try:
            token_key = request.data['token']
            token = Token.objects.filter(key = token_key).first()
            
            if token:
                user = token.user
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now()) #Searches all the opened sessions
                
                #Deletes sessions if they exist
                if all_sessions.exists(): 
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == session_data.get('auth_user_id'):
                            session.delete() 
                #Finally deletes token
                token.delete() 
                
                return Response({'message':'Session closed.'}, status.HTTP_200_OK)
        
        except Token.DoesNotExist:
            return Response({'message':'Token not found.'}, status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
