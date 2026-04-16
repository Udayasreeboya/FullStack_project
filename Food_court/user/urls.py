from django.urls import path
from .views import login_view, signup_view, forgot_password

urlpatterns = [
    path('login/', login_view),
    path('signup/', signup_view),
    path('forgot/', forgot_password),
]