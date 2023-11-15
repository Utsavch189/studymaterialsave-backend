from django.urls import path
from apps.users.controller.getAllSharesController import GetAllSharesController
from apps.users.controller.getUserController import GetAUser

urlpatterns = [
    path('get-all-shares/',GetAllSharesController.as_view()),
    path('get-user/',GetAUser.as_view())
]
