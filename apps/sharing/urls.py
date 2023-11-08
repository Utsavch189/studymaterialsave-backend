from django.urls import path
from apps.sharing.controller.sectionShareController import SectionShareController

urlpatterns = [
    path('share-section/',SectionShareController.as_view()),
]
