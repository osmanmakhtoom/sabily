from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Sabily API",
        default_version="v1",
        description="The full Islamic religious App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="osmanmakhtoom@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[JWTAuthentication],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger.<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "api/v1/account/",
        include(("apps.account.api.v1.urls", "account"), namespace="v1"),
    ),
    path(
        "api/v1/charity/",
        include(("apps.charity.api.v1.urls", "charity"), namespace="v1"),
    ),
    path(
        "api/v1/events/",
        include(("apps.events.api.v1.urls", "events"), namespace="v1"),
    ),
]
