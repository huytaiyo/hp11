from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required   
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db.utils import OperationalError, ProgrammingError

from .forms import RegisterForm
from .models import Product, Category

def home_view(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('cat', '').strip()
    
    product = []
    categories = []
    
    try :
        qs = Product.objects.filter(is_active=True)
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        product = list(qs[:48])
        categories = list(Category.objects.all())
        categories_tiles = []
        for cat in categories:
            if getattr(cat, 'image_url', None):
                thumb = cat.image_url
            else:
                first_with_img = Product.objects.filter(category=cat, image_url__isnull=False).first()
                if first_with_img and first_with_img.image_url:
                    thumb = first_with_img.image_url
                else:
                    initials = (cat.name or "?")[:1].upper()
                    thumb = f"https://via.placeholder.com/150?text={initials}"
            categories_tiles.append({
                'name': cat.name,
                'slug': cat.slug,
                'image_url': thumb,
            })
    except (OperationalError, ProgrammingError):
        messages.warning(request, "Database is not ready. Please run migrations.")
        categories_tiles = []
        
    context = {
        'products': product,
        'categories': categories,
        'current_query': query,
        'current_category': category_slug,
        'categories_tiles': categories_tiles,
    }
    
    return render(request, 'shop/home.html', context)
def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(is_active=True, category=product.category).exclude(id=product.id)[:8]
    context = {
        'product': product,
        'related_products': related,
    }
    return render(request, 'shop/product_detail.html', context)

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
     