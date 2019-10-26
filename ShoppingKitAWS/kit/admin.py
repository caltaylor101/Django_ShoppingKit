from django.contrib import admin
from .models import KitPost
# Register your models here.


class KitPostAdmin(admin.ModelAdmin):
    save_as = True

admin.site.register(KitPost, KitPostAdmin)