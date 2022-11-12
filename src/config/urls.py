from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings
from core.views import Forbidden, PageNotFound

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("catalogue/", include("catalogue.urls")),
    path("mongo/", include("mongo.urls")),
    path("user/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
]

if settings.dev.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
    urlpatterns += static(settings.dev.MEDIA_URL, document_root=settings.dev.MEDIA_ROOT)
    urlpatterns += static(settings.dev.STATIC_URL, document_root=settings.dev.STATIC_ROOT)


handler404 = PageNotFound.as_view()
handler403 = Forbidden.as_view()
