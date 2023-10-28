from django.urls import path
from .controller.register_controller import Register
from .controller.login_controller import Login
from .controller.logout_controller import Logout


urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view())
]
