from django.contrib import admin
from apps.sharing.models.sharedSections import SharedSection
from apps.sharing.models.sharedPosts import SharedPost

admin.site.register(SharedSection)
admin.site.register(SharedPost)