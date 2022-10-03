"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from app.views import UserViewSet
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('listdata', UserViewSet, basename='listdata')
# router.register('pdftojson', PdftoJson, basename='pdftojson')
urlpatterns = router.urls



schema_view = get_schema_view(
    openapi.Info(
        title="Candidate API",
        default_version='v1',
        description="Welcome to the world of sort Candidate",
        terms_of_service="https://www.candidate.org",
        contact=openapi.Contact(email="candidate@candidate.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here

    path('',include(router.urls)),
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('json/',include('app.urls')),
    path('ptoj/',include('PDFtoJson.urls')),
    path('data/',include('Checkdata.urls')),
]
