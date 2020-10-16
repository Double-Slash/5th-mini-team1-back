from django.contrib import admin
from .models import *


class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content', 'time')
    ordering = ('-time', )


admin.site.register(Chat, ChatAdmin)


