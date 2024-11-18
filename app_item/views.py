from django.shortcuts import render, redirect, get_object_or_404
from .models import tb_item, tb_category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.db.models import Q


def items(request):
    items = tb_item.objects.filter(is_sold = False)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = tb_category.objects.all()

    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__contains = query) | Q(description__icontains = query))

    return render(request, 'app_item/items.html', {
        'items' : items,
        'query' : query, 
        'categories' : categories, 
        'category' : int(category_id), 
    })

def detail(request, pk):
    item = get_object_or_404(tb_item, pk=pk)
    related_items = tb_item.objects.filter(category=item.category, is_sold = False).exclude(pk = pk)[0:3]

    return render(request, 'app_item/detail.html', {
        'item' : item,
        'related_items' : related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('app_item:detail', pk = item.id)
    else:
        form = NewItemForm()

    return render(request, 'app_item/form.html', {
        'form' : form, 
        'title' : 'New item', 
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(tb_item, pk = pk, created_by = request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance = item)

        if form.is_valid():
            form.save()

            return redirect('app_item:detail', pk = item.id)
    else:
        form = EditItemForm(instance = item)

    return render(request, 'app_item/form.html', {
        'form' : form, 
        'title' : 'New item', 
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(tb_item, pk = pk, created_by = request.user)
    item.delete()

    return redirect('app_dashboard:index')
