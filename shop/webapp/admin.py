from django.contrib import admin

# Register your models here.
from webapp.models import Product, ProductBasket, Order, OrderProduct

admin.site.register(Product)
admin.site.register(ProductBasket)

admin.site.register(OrderProduct)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'author', 'created_at']
#     list_filter = ['author']
#     search_fields = ['title', 'content']
#     fields = ['title', 'author', 'content', 'created_at', 'updated_at']
#     readonly_fields = ['created_at', 'updated_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'phone', 'created_at']
    search_fields = ['-created_at']
    fields = ['address', 'phone', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Order, OrderAdmin)
