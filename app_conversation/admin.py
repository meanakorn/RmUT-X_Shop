from django.contrib import admin

from .models import tb_conversation, tb_conversation_message

admin.site.register(tb_conversation)
admin.site.register(tb_conversation_message)

