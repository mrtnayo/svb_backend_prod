from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


admin.site.site_header = "SISTEMA DE VENTA PARA BODEGAS"
admin.site.site_title = "SISTEMA DE VENTA PARA BODEGAS Admin Portal"
admin.site.index_title = "BIENVENIDOS AL ADMINISTRADOR DE SVB 1.0"


schema_view = get_schema_view(
    openapi.Info(
        title="SVB API Documentation",
        default_version='v1',
        description="Documentación para el API de SVB.",
        terms_of_service="",
        contact=openapi.Contact(email="mrtnayo@gmail.com"),
        license=openapi.License(name="Powered by MAC"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^docs/redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    re_path(r'admin/', admin.site.urls),
    path('auth/', include('apps.rest_auth.urls')),
    path('api/products/', include('apps.products.urls')),
    #     path('api/orders/', include('apps.orders.urls'))
]
