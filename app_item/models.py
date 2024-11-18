from django.db import models
from django.contrib.auth.models import User


class tb_category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'tb_categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

class tb_item(models.Model):
    category = models.ForeignKey(tb_category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

