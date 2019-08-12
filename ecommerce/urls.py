from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
# from products.views import ProductListView, product_list_view, ProductDetailView, ProductDetailSlugView, product_detail_view, ProductFeaturedListView, ProductFeaturedDetailView

from addresses.views import checkout_address_create_view

from accounts.views import RegisterView, guest_register, LoginView
from .views import home_page, about_page, contact_page
from carts.views import cart_detail_api_view

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('admin/', admin.site.urls),
    path('api/cart/', cart_detail_api_view, name="api-cart"),
    path('checkout/address/create', checkout_address_create_view,
         name="checkout_address_create"),
    path('register/guest', guest_register, name="guest_register"),
    path('products/', include(("products.urls", "products"), namespace="products")),
    path('search/', include(("search.urls", "search"), namespace="search")),
    path('cart/', include(("carts.urls", "carts"), namespace="cart")),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
