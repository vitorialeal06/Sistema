from django.contrib import admin
from django.urls import include, path
from sistema import settings
from django.conf.urls.static import static
from sistema.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('veiculo/', include('veiculo.urls'), name = 'veiculo')
]

#if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)