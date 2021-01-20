from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('cv/', include('cv.urls', namespace='cv')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('caparu/', include('caparu.urls', namespace='caparu')),
    path('tftsd/', include('tftsd.urls', namespace='tftsd')),
    path('dbt/', include('dbt.urls', namespace='dbt')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
