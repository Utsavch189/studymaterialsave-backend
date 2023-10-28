from django.urls import path,re_path
from .controller.section_controller import SectionController

urlpatterns = [
    re_path(r'^sections/$',SectionController.as_view()),
    re_path(r'^sections/(?P<id>[\s\S]*)/$',SectionController.as_view())
]
