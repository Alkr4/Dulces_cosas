from django.contrib import admin
from Products.models import Product, Category, Supplier, RawMaterial
from Accounts.models import Profile, Role
from Sells.models import Client, Location, Warehouse


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'category', 'current_stock', 'min_stock', 'max_stock')
    search_fields = ('name', 'sku')
    list_filter = ('category',)
    ordering = ('name',)
    list_select_related = ('category',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('bussiness_name', 'rut', 'email', 'phone')
    search_fields = ('bussiness_name', 'rut', 'email', 'phone')
    ordering = ('bussiness_name',)

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock_quantity', 'expiration_date')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'privilege_level')
    search_fields = ('name',)
    ordering = ('privilege_level',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'run', 'phone', 'role')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'run', 'phone', 'role__name')
    list_filter = ('role',)
    ordering = ('user__username',)
    list_select_related = ('user', 'role')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('bussiness_name', 'rut', 'email', 'credit_limit', 'max_debt', 'is_suspended')
    search_fields = ('bussiness_name', 'rut', 'email')
    list_filter = ('is_suspended',)
    ordering = ('bussiness_name',)
    list_select_related = ('warehouse',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    ordering = ('name',)
    list_select_related = ('city',)

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'total_area', 'location')
    search_fields = ('name', 'address', 'location__name')
    list_filter = ('location',)
    ordering = ('name',)
    list_select_related = ('location',)
    