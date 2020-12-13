from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Categories, Store, CategoriesProd, ProductStore, Customer, Ubicacion
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'


class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoriesProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProductStoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Ubicacion)
class Ubicacion(LeafletGeoAdmin):
    list_display = ('point', 'location')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(CategoriesProd, CategoriesProdAdmin)
admin.site.register(Customer)
admin.site.register(ProductStore, ProductStoreAdmin)
