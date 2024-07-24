from django.contrib import admin
from django.urls import path, include
from . import settings 
from django.conf.urls.static import static 
from django.conf.urls import handler404
from Home_App.views import error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home_App.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error
