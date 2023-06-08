from django.urls import path
from . import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', user_views.register, name='gossip-register'),
    path('profile/', user_views.profile, name='gossip-profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
