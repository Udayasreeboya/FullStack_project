from django.urls import path
from .views import signup, login_user, forgot_password

urlpatterns = [
    path('signup/', signup),
    path('login/', login_user),
    path('forgot-password/', forgot_password),
]