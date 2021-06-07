
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'homepage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('after_log/', include('after_log.urls')),
    path('auth_page/', include('auth_page.urls')),
    path('album_details/', include('album_details.urls')),
    path('file_upload/', include('file_upload.urls')),
    path('search/', include('search.urls')),
    path('account/', include('account.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)