from django.contrib import admin
from webapp.models import Register


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'text', 'status', 'create', 'update']
    list_filter = ['status']
    list_display_links = ['author']
    search_fields = ['author']
    exclude = []


admin.site.register(Register, RegisterAdmin)


