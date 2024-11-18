from django import forms

from .models import tb_conversation_message

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = tb_conversation_message
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'w-full px-6 py-4 rounded-xl border'
            })
        }
