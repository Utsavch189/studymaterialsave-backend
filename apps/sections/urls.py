from django.urls import path,re_path
from .controller.section_controller import SectionController



urlpatterns = [
    re_path(r'',SectionController.as_view())
]
