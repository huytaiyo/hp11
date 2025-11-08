from django.contrib import admin
from .models import Category, Product, Banner
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    fields = ('name', 'slug', 'image_url')
    
    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="height:31px;width:32px;object-fit:cover;border-radius:4px;" />', obj.image_url)
        return "No Image"
    image_preview.short_description = 'Image_Preview'
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'created_at')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldssets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'description', 'price', 'stock', 'is_active', 'image_url', 'color_options', 'specifications')
        }),
        ('image, storge', {
            'fields': ('image_url','stock'),
        }),
        ('mota & thuoc tinh',{
            'fields': ('description', 'color_options', 'specifications'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_featured', 'created_at', 'image_preview', 'discount_info')
    list_filter = ('is_active', 'is_featured')
    search_fields = ('title', 'discount_info')
    fields = ('title', 'image_url', 'link', 'is_active', 'is_featured', 'discount_info')
    
    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="height:50px;width:100px;object-fit:cover;border-radius:4px;" />', obj.image_url)
        return "No Image"
    image_preview.short_description = 'Image Preview'