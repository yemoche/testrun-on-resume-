from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('resume/', views.home, name='home'),
    path('contact/', views.contact, name='index'),
    path('demo/', views.demo, name='demo'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
