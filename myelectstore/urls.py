from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storefront.urls')),       # الصفحة الرئيسية
    path('products/', include('catalog.urls')), # صفحة عرض المنتجات
    path('checkout/', include('checkout.urls')), # صفحة الدفع أو السلة
]

# لتقديم ملفات الوسائط (مثل صور المنتجات) خلال وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
