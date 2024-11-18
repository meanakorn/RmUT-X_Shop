from django.shortcuts import render, redirect
from app_item.models import tb_category, tb_item
from .forms import SignupForm


def index(request):
    items = tb_item.objects.filter(is_sold = False) [0:6]
    categories = tb_category.objects.all()

    return render(request, 'app_core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'app_core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'app_core/signup.html', {
        'form' : form 
    })
