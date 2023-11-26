from django.urls import path
from .controller.register_controller import Register
from .controller.login_controller import Login
from .controller.logout_controller import Logout
from .controller.refreshToken_controller import RefreshToken


urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('refresh-token/',RefreshToken.as_view())
]
