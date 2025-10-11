from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required   
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.utils import OperationalError, ProgrammingError

from .forms import RegisterForm
from .models import Product, Category

def home_view(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('cat', '').strip()
    
    product = []
    catagories = []
    
    try :
        qs = Product.objects.filter(is_active=True)
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        product = list(qs[:48])
        catagories = list(Category.objects.all())
    except (OperationalError, ProgrammingError):
        messages.warning(request, "Database is not ready. Please run migrations.")
    
    context = {
        'products': product,
        'categories': catagories,
        'current_query': query,
        'current_category': category_slug,
    }
    
    return render(request, 'shop/home.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
        
    return render(request, 'registration/register.html', {'form': form})
     