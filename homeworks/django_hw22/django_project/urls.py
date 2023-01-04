from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import upload_picture


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('products/', include("products.urls")),
    path('category/', include("products.urls")),
    path('upload_picture', upload_picture, name = "files" )
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)