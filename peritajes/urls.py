from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from peritajes_app.views import generar_pdf, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('generar_pdf/', generar_pdf, name="generar_pdf"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
