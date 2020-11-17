from django.contrib import admin
from .models import Categories, Store, CategoriesProd, ProductStore, Customer


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoriesProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CustomerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'id': ('firstname',)}


class ProductStoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Store, StoreAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(CategoriesProd, CategoriesProdAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ProductStore, ProductStoreAdmin)
