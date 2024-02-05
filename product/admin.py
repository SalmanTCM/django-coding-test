from django.contrib import admin
from .models import Variant, Product, ProductImage, ProductVariant, ProductVariantPrice

class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    list_display_links = ('title', 'description')
    list_filter = ('created_at', 'updated_at') 
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    list_per_page = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sku', 'created_at', 'updated_at')
    list_display_links = ('title', 'sku')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'sku')
    list_per_page = 2

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'file_path', 'created_at', 'updated_at')
    list_display_links = ('product', 'file_path')
    list_filter = ('product', 'created_at', 'updated_at')
    search_fields = ('product__title', 'file_path')
    list_per_page = 2

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant_title', 'variant', 'product', 'created_at', 'updated_at')
    list_display_links = ('variant_title', 'variant', 'product')
    list_filter = ('variant_title', 'created_at', 'updated_at')
    search_fields = ('variant_title', 'variant__title', 'product__title')
    list_per_page = 2

class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock', 'product', 'created_at', 'updated_at')
    list_display_links = ('price', 'stock', 'product')
    list_filter = ('price', 'created_at', 'updated_at')
    search_fields = ('product_variant_one__variant_title', 'product_variant_two__variant_title', 'product_variant_three__variant_title', 'price', 'stock', 'product__title')
    list_per_page = 2

admin.site.register(Variant, VariantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
