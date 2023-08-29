"""seasons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include 
from . import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header  =  " !!! Administrator_Portal !!! "  
admin.site.site_title  =  " !!! Administrator_Portal !!! "
admin.site.index_title  =  "!!! Administrator_Page !!!"
admin.site.site_url = ''' <link rel="shortcut icon" href="/static/image/favicon.ico" type="image/x-icon">'''



urlpatterns = [
    path('admin/',admin.site.urls),
    path('summer/',views.summer,name='summer'),
    path('',views.home,name='home'),
    path('winter/',views.winter,name='winter'),
    path('autumn/',views.autumn,name='autumn'),
    path('spring/',views.spring,name='spring'),
    path('climate/',include('climate.urls')),
    path('index/',views.index,name='index'),
    path('imageuploader/',views.imageuploader,name='imageuploader'),
    path('base/',views.base,name='base'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



