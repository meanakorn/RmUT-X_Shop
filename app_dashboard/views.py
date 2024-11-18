from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app_item.models import tb_item

@login_required
def index(request):
    items = tb_item.objects.filter(created_by = request.user)

    return render(request, 'app_dashboard/index.html', {
        'items' : items, 
    })
