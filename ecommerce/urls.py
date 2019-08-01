from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
# from products.views import ProductListView, product_list_view, ProductDetailView, ProductDetailSlugView, product_detail_view, ProductFeaturedListView, ProductFeaturedDetailView
from accounts.views import login_page, register_page, guest_register
from .views import home_page, about_page, contact_page


urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
    path('register/guest', guest_register, name="guest_register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', register_page, name="register"),
    path('admin/', admin.site.urls),
    path('products/', include(("products.urls", "products"), namespace="products")),
    path('search/', include(("search.urls", "search"), namespace="search")),
    path('cart/', include(("carts.urls", "carts"), namespace="cart")),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
