from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(('lettings.urls', 'lettings'), 'lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), 'profiles')),
    path('admin/', admin.site.urls),
    path('raise_500', views.raise_500, name='raise_500'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
