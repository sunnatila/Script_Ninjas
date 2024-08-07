from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

schema_view = get_schema_view(
   openapi.Info(
      title="Script Ninjas API",
      default_version='v1',
      description="Script Ninjas Team API",
      terms_of_service="",
      contact=openapi.Contact(email="script_nijas@gmail.com"),
      license=openapi.License(name="SNT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', include('home_page.urls')),
]
urlpatterns += i18n_patterns(

   path('set_language/', set_language, name='set_language'),
   path('api/v1/', include('users.urls')),
)