from django.contrib import admin
from django.urls import path

from users import views as user_views
from menu import views as menu_views
from cart import views as cart_views
from orders import views as order_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', menu_views.menu_list, name="home"),

    path('add-to-cart/<int:id>/', cart_views.add_to_cart, name="add_to_cart"),
    path('cart/', cart_views.cart_view, name="cart"),

    path('increase/<int:id>/', cart_views.increase_qty, name="increase"),
    path('decrease/<int:id>/', cart_views.decrease_qty, name="decrease"),

    path('place-order/', order_views.place_order, name="place_order"),
    path('orders/', order_views.order_history, name="orders"),

    path('login/', user_views.user_login, name="login"),
    path('signup/', user_views.signup, name="signup"),
    path('logout/', user_views.user_logout, name="logout"),
    path('remove/<int:id>/', cart_views.remove_item, name="remove"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)