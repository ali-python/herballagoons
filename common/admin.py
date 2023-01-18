from django.contrib import admin
from .models import Registration, Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'image'
    )

admin.site.register(Registration)
admin.site.register(Gallery,GalleryAdmin)

