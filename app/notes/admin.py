from django.contrib import admin
from .models import Notes


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'user_key')
    search_fields = ('title',)
    list_filter = ('title', 'created', 'user_key')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Notes, NotesAdmin)
