from rest_framework.routers import DefaultRouter

from apps.account.api.views import UserViewSet, TokenViewSet

router = DefaultRouter(trailing_slash=False)

router.register("users", UserViewSet, basename="users")
router.register("tokens", TokenViewSet, basename="tokens")

urlpatterns = router.urls
