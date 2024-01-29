# from datetime import timedelta
# from django.utils import timezone
# from django.conf import settings
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.exceptions import AuthenticationFailed

# class ExpiringTokenAuthentication(TokenAuthentication):
#     def expires_in(self, token):
#         time_elapsed = timezone.now() - token.created
#         left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS - time_elapsed)
#         return left_time
        
#     def is_token_expired(self, token):
#         return self.expires_in(token) < timedelta(seconds = 0)
    
#     def token_expire_handler(self,token):
#         is_expire = self.is_token_expired(token)
#         if is_expire:
#             print('TOKEN EXPIRADO')
        
#         return is_expire
    
#     def authenticate_credentials(self, key):
#         try:
#             token = self.get_model().objects.get(key = key)
        
#         except self.get_model.DoesNotExist(): 
#             raise AuthenticationFailed('Invalid token.')
        
#         if not token.user.is_active:
#             raise AuthenticationFailed('User not active or deleted.')
        
#         is_expired = self.token_expire_handler(token)
        
#         if is_expired: 
#             raise AuthenticationFailed('Your token has expired')
        
#         return (token.user, token)