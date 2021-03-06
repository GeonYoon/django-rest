"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # accounts app 


# app_name = 'api-user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(('accounts.api.urls','api-auth'))),
    path('api/user/', include(('accounts.api.user.urls','api-user'))),
    path('api/', include('rest_framework.urls')),
    path('api/status/',include(('status.api.urls','api-status'))),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
