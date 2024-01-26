from rest_framework.routers import DefaultRouter
from users.api.views import UsersSignInViewSet

router = DefaultRouter()

router.register(r'signin', UsersSignInViewSet, basename='sign_in')


urlpatterns = router.urls