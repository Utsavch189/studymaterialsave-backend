from django.urls import path
from apps.users.controller.getAllSharesController import GetAllSharesController

urlpatterns = [
    path('get-all-shares/',GetAllSharesController.as_view())
]
