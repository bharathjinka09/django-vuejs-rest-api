from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('lists/', include('apps.lists.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)