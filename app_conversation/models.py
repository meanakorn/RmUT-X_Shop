from django.db import models
from django.contrib.auth.models import User

from app_item.models import tb_item

class tb_conversation(models.Model):
    item = models.ForeignKey(tb_item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-modified_at',)

class tb_conversation_message(models.Model):
    conversation = models.ForeignKey(tb_conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

