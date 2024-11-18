from django.contrib import admin

from .models import tb_category, tb_item

admin.site.register(tb_category)
admin.site.register(tb_item)

