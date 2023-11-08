from django.urls import path
from apps.sharing.controller.sectionShareController import SectionShareController
from apps.sharing.controller.postShareController import PostShareController

urlpatterns = [
    path('share-section/',SectionShareController.as_view()),
    path('share-post/',PostShareController.as_view()),
]
