from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, AffiliateLink, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    display_image.short_description = 'Image'

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class AffiliateLinkInline(admin.TabularInline):
    model = AffiliateLink
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available', 'is_featured', 'display_image')
    list_filter = ('category', 'is_available', 'is_featured', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, AffiliateLinkInline]
    list_editable = ('is_available', 'is_featured', 'stock')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    display_image.short_description = 'Image'

@admin.register(AffiliateLink)
class AffiliateLinkAdmin(admin.ModelAdmin):
    list_display = ('product', 'platform', 'commission_rate', 'clicks', 'created_at')
    list_filter = ('platform', 'created_at')
    search_fields = ('product__name', 'platform')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'display_image', 'alt_text', 'is_feature')
    list_filter = ('is_feature', 'created_at')
    search_fields = ('product__name', 'alt_text')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    display_image.short_description = 'Image'