from django import forms
from .models import tb_item

INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = tb_item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'name' : forms.TimeInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = tb_item
        fields = ('name', 'description', 'price', 'image', 'is_sold',)
        widgets = {
            'name' : forms.TimeInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }
